import requests

class HomeAssistantAPI:
    def __init__(self, url, token):
        self.url = url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def call_service(self, domain, service, data=None):
        endpoint = f"{self.url}/api/services/{domain}/{service}"
        r = requests.post(endpoint, headers=self.headers, json=data or {})
        try:
            r.raise_for_status()
        except requests.HTTPError:
            return {"success": False, "error": r.text}
        return {"success": True, "data": r.json()}



# import requests

# class HomeAssistantAPI:
#     def __init__(self, url, token):
#         self.url = url.rstrip("/")
#         self.headers = {
#             "Authorization": f"Bearer {token}",
#             "Content-Type": "application/json",
#         }

#     def call_service(self, domain, service, data=None):
#         endpoint = f"{self.url}/api/services/{domain}/{service}"
#         response = requests.post(endpoint, headers=self.headers, json=data or {})

#         # Raise exceptions if HA returned an error
#         try:
#             response.raise_for_status()
#         except requests.HTTPError as e:
#             return {
#                 "success": False,
#                 "error": str(e),
#                 "response": response.text
#             }

#         return {
#             "success": True,
#             "data": response.json()
#         }

#     def get_states(self):
#         endpoint = f"{self.url}/api/states"
#         response = requests.get(endpoint, headers=self.headers)

#         try:
#             response.raise_for_status()
#         except requests.HTTPError as e:
#             return {
#                 "success": False,
#                 "error": str(e),
#                 "response": response.text
#             }

#         return {
#             "success": True,
#             "data": response.json()
#         }

#     def call_entity_service(self, entity_id, service, domain=None, **kwargs):
#         """
#         Helper function for typical commands like:
#         light.turn_on, vacuum.start, switch.toggle
#         """
#         if domain is None:
#             domain = entity_id.split(".")[0]  # infer domain automatically

#         data = {"entity_id": entity_id}
#         data.update(kwargs)

#         return self.call_service(domain, service, data)
