# 第 85 轮 Vitesse Python 规则自测:前半为必须检出,后半为必须放行
import kcs_util

# [违规] f-string (Py3)
x = f"{a} mm"
msg = f'result={v}'

# [违规] Py3 类型注解
def calc(a: int, b: str) -> float:
    return 0.0

# [合法] %f 格式串(官方大量)
print '%f' % x
y = '%.2f' % v
z = '%6.2f' % w

# [合法] 字符串尾部 f / 普通字符串
name = "format f"
tag = 'f'
units = 'mmf'

# [合法] Py2 print 语句 / except 逗号式
try:
    kcs_draft.dwg_new(n, f, t)
except Exception, e:
    print e

# [合法] 行内注释含 f'
# note: this is not f'string'
print 'ok'
