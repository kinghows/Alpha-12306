# 关于软件使用配置说明，一定要看！！！
# ps: 如果是候补车票，需要通过人证一致性核验的用户及激活的“铁路畅行”会员可以提交候补需求，请您按照操作说明在铁路12306app.上完成人证核验
# 关于候补了之后是否还能继续捡漏的问题在此说明： 软件为全自动候补加捡漏，如果软件候补成功则会停止抢票，发出邮件通知，但是不会影响你继续捡漏，
# 如果这个时候捡漏捡到的话，也是可以付款成功的，也就是说，捡漏+候补，可以最大程度提升抢票成功率
import configparser

config_file="12306.ini"
config = configparser.ConfigParser()
config.read(config_file)
# 刷票模式：1=刷票 2=候补+刷票
TICKET_TYPE = int(config.get("TICKET_SET","TICKET_TYPE"))

# 出发日期(list) "2018-01-06", "2018-01-07"
STATION_DATES = config.get("TICKET_SET","STATION_DATES").split(",") 

# 预售放票时间, 如果是捡漏模式，可以忽略此操作
OPEN_TIME = config.get("TICKET_SET","OPEN_TIME")

# 填入需要购买的车次(list)，"G1353"
# 修改车次填入规则，注：(以前设置的车次逻辑不变)，如果车次填入为空，那么就是当日乘车所有车次都纳入筛选返回
STATION_TRAINS = config.get("TICKET_SET","STATION_TRAINS").split(",") 

# 出发城市，比如深圳北，就填深圳就搜得到
FROM_STATION = config.get("TICKET_SET","FROM_STATION")

# 到达城市 比如深圳北，就填深圳就搜得到
TO_STATION = config.get("TICKET_SET","TO_STATION")

# 座位(list) 多个座位ex:一等座,二等座
SET_TYPE = config.get("TICKET_SET","SET_TYPE").split(",") 

# 当余票小于乘车人，如果选择优先提交，则删减联系人和余票数一致在提交
IS_MORE_TICKET = bool(config.get("TICKET_SET","IS_MORE_TICKET"))

# 乘车人(list) 多个乘车人ex:张三,李四
TICKET_PEOPLES = config.get("TICKET_SET","TICKET_PEOPLES").split(",") 

# 12306登录账号
USER = config.get("12306_SET","USER")
PWD = config.get("12306_SET","PWD")

#  邮箱配置，如果抢票成功，将通过邮件配置通知给您
EMAIL_CONF = {}
EMAIL_CONF['IS_MAIL'] = bool(config.get("EMAIL_SET","IS_MAIL"))
EMAIL_CONF['email'] = config.get("EMAIL_SET","email")
EMAIL_CONF['notice_email_list'] = config.get("EMAIL_SET","notice_email_list")
EMAIL_CONF['username'] = config.get("EMAIL_SET","username")
EMAIL_CONF['password'] = config.get("EMAIL_SET","password")
EMAIL_CONF['host'] = config.get("EMAIL_SET","host")

# 是否开启 server酱 微信提醒， 使用前需要前往 http://sc.ftqq.com/3.version 扫码绑定获取 SECRET 并关注获得抢票结果通知的公众号
SERVER_CHAN_CONF = {}
SERVER_CHAN_CONF['is_server_chan'] = bool(config.get("SERVER_CHAN_SET","is_server_chan"))
SERVER_CHAN_CONF['secret'] = config.get("SERVER_CHAN_SET","secret")

# 加入小黑屋时间默认为5分钟，此功能为了防止僵尸票导致一直下单不成功错过正常的票
TICKET_BLACK_LIST_TIME = config.get("SOFT_SET","TICKET_BLACK_LIST_TIME")

# 自动打码
IS_AUTO_CODE = bool(config.get("SOFT_SET","IS_AUTO_CODE"))

# 是否开启cdn查询，可以更快的检测票票 1为开启，2为关闭
IS_CDN = int(config.get("SOFT_SET","IS_CDN"))

# 下单接口分为两种，1 模拟网页自动捡漏下单（不稳定），2 模拟车次后面的购票按钮下单（稳如老狗）
ORDER_TYPE = int(config.get("SOFT_SET","ORDER_TYPE"))
# 下单模式 1 为预售，整点刷新，刷新间隔0.1-0.5S, 然后会校验时间，比如12点的预售，那脚本就会在12.00整检票，刷新订单
#         2 是捡漏，捡漏的刷新间隔时间为0.5-3秒，时间间隔长，不容易封ip
ORDER_MODEL = int(config.get("SOFT_SET","ORDER_MODEL"))

# 是否开启代理, 0代表关闭， 1表示开始
IS_PROXY = int(config.get("SOFT_SET","IS_PROXY"))

# 1=使用selenium获取devicesID
# 2=使用网页端/otn/HttpZF/logdevice获取devicesId，这个接口的算法目前可能有点问题，如果登录一直302的请改为配置1
COOKIE_TYPE = int(config.get("SOFT_SET","COOKIE_TYPE"))
# 如果COOKIE_TYPE=1，则需配置chromeDriver路径,下载地址http://chromedriver.storage.googleapis.com/index.html
# chromedriver配置版本只要和chrome的大版本匹配就行

# 1=>为一直随机ua,2->只启动的时候随机一次ua
RANDOM_AGENT = int(config.get("SOFT_SET","RANDOM_AGENT"))

# 保护12306官网请求频率，设置随机请求时间，原则为5分钟不大于80次
# 最大间隔请求时间
MAX_TIME = int(config.get("SOFT_SET","MAX_TIME"))

# 最小间隔请求时间
MIN_TIME = int(config.get("SOFT_SET","MIN_TIME"))

PASSENGER_TICKER_STR = {
    '一等座': 'M',
    '特等座': 'P',
    '二等座': 'O',
    '商务座': 9,
    '硬座': 1,
    '无座': 1,
    '软座': 2,
    '软卧': 4,
    '硬卧': 3,
    }

# 软件版本
RE_VERSION = "1.1.113"
