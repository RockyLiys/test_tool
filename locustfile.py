from locust import HttpLocust, TaskSet, task, Locust
def index(l):
    l.client.get("/ws/mapapi/mx/poi/search?pagesize=15&query_type=RQBXY&longitude=121.498588&latitude=31.235187&range=10000&sort_rule=10000&channel=jlr_new&sign=713025D692C772BF6B4E4D3E5CC4D271&language=zh_cn&category=150900")

class UserBehavior(TaskSet):
    tasks = {index: 1 }

    def on_start(self):
        index(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://telematics.autonavi.com"
    min_wait = 0
    max_wait = 0
