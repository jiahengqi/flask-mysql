#coding:utf-8
import numpy as np
from locust import HttpLocust, TaskSet, task
 
class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.client.get("/")

    @task(1)
    def index(self):
        self.client.get("/")

    # @task(3)
    # def login(self):
    #     self.client.post("/login_request",{'password':'123','username':'qwe'})

    # @task(10)
    # def get_all(self):
    #     self.client.get("/all")

    @task(5)
    def register(self):
        self.client.post("/signup_request",{'username':'randm'+str(np.random.randint(1,1000000)),'password':'123','password2':'123'})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host='http://127.0.0.1:7086'
    min_wait = 5000
    max_wait = 10000