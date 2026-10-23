using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.EditorInput;
using Autodesk.AutoCAD.Runtime;
using OfficeOpenXml;

namespace CadPidExportPlugin
{
    public class CadPidExportCommands
    {
        private static readonly Regex PipeIdRegex = new Regex(
            @"(?<![A-Z0-9])(?<pid>\d{1,4}-[A-Z]{2}-\d{3,6}-[A-Z0-9]{2,5})(?![A-Z0-9])",
            RegexOptions.IgnoreCase | RegexOptions.Compiled
        );

        [CommandMethod("PIDXLS")]
        public void ExportPidToExcelCommand()
        {
            ExportPidToExcel();
        }

        [CommandMethod("CADPID")]
        public void ExportPidToExcelAltCommand()
        {
            ExportPidToExcel();
        }

        private static void ExportPidToExcel()
        {
            var doc = Application.DocumentManager.MdiActiveDocument;
            if (doc == null)
            {
                return;
            }

            var ed = doc.Editor;
            var db = doc.Database;
            var pipes = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

            using (var tr = db.TransactionManager.StartTransaction())
            {
                var bt = (BlockTable)tr.GetObject(db.BlockTableId, OpenMode.ForRead);
                foreach (var btrId in bt)
                {
                    var btr = (BlockTableRecord)tr.GetObject(btrId, OpenMode.ForRead);
                    if (btr == null)
                    {
                        continue;
                    }

                    foreach (ObjectId id in btr)
                    {
                        var obj = tr.GetObject(id, OpenMode.ForRead);
                        ExtractFromEntity(obj, pipes);
                    }
                }

                tr.Commit();
            }

            if (pipes.Count == 0)
            {
                ed.WriteMessage("\nNo PID values found in current drawing.\n");
                return;
            }

            var items = pipes
                .OrderBy(x => x, StringComparer.OrdinalIgnoreCase)
                .ToList();

            var outputPath = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
                "cad_pid_export.xlsx"
            );

            using (var package = new OfficeOpenXml.ExcelPackage())
            {
                var ws = package.Workbook.Worksheets.Add("PID");
                ws.Cells[1, 1].Value = "PID";
                ws.Cells[1, 2].Value = "FORMATTED";

                for (int i = 0; i < items.Count; i++)
                {
                    var pid = items[i];
                    ws.Cells[i + 2, 1].Value = pid;
                    ws.Cells[i + 2, 2].Value = FormatPid(pid);
                }

                ws.Column(1).Width = 22;
                ws.Column(2).Width = 60;
                ws.Cells[ws.Dimension.Address].AutoFitColumns();
                package.SaveAs(new FileInfo(outputPath));
            }

            ed.WriteMessage($"\nExported {items.Count} PID records to: {outputPath}\n");
        }

        private static void ExtractFromEntity(DBObject obj, HashSet<string> pipes)
        {
            if (obj is DBText txt)
            {
                AddMatches(txt.TextString, pipes);
            }
            else if (obj is MText mtext)
            {
                AddMatches(mtext.Contents, pipes);
            }
            else if (obj is AttributeReference att)
            {
                AddMatches(att.TextString, pipes);
            }
        }

        private static void AddMatches(string text, HashSet<string> pipes)
        {
            if (string.IsNullOrWhiteSpace(text))
            {
                return;
            }

            foreach (Match match in PipeIdRegex.Matches(text))
            {
                var pid = match.Groups["pid"].Value.Trim();
                if (!string.IsNullOrWhiteSpace(pid))
                {
                    pipes.Add(pid.ToUpperInvariant());
                }
            }
        }

        private static string FormatPid(string pid)
        {
            var suffix = pid.Split('-').Last();
            return $"NEW PIPE /{pid} PSPEC /{suffix}";
        }
    }
}
