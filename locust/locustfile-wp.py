from locust import HttpUser, TaskSet, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")

    @task
    def login_page(self):
        self.client.get("/wp/wp-login.php")

    @task()
    def search_for_blog_post(self):
        self.client.get("/?s=hello+world")

    @task()
    def search_for_blog_unpost(self):
        self.client.get("/?s=test")

#     @task
#     def posts(self):
#         for i in range(1, 200, 1):
#             self.client.get(f"/?page_id={i}")
