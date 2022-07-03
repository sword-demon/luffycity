# Create your models here.
from models import models, BaseModel


class Nav(BaseModel):
    """
    导航菜单
    """

    # 菜单位置选项
    # 模型对象.<字段名> 获取实际数据
    # 模型对象.get_<字段名>_display*() # 获取文本内容
    POSITION_OPTIONS = (
        # （实际数据, "文本提示"),
        (0, '顶部菜单'),
        (1, '底部菜单'),
    )

    link = models.CharField(max_length=255, verbose_name='导航链接')
    is_http = models.BooleanField(default=False, verbose_name='是否是外部链接')
    position = models.IntegerField(choices=POSITION_OPTIONS, default=0)

    class Meta:
        # 设置表名
        db_table = "lf_nav"
        # 表名注释
        verbose_name = "导航菜单"
        # 复数形式和单数形式一样的
        verbose_name_plural = verbose_name
