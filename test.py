
# importing the requests library
import requests
import matplotlib.pyplot as plt
  
# api-endpoint
URL = "https://ghoapi.azureedge.net/api/WHOSIS_000001"
  
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# extracting data in json format
data = r.json()

print(data["value"][0])

Id_array = []
value_array = []
for i in range(len(data["value"])):
    Id_array.append(data["value"][i]["TimeDim"])
    value_array.append(data["value"][i]["Value"])

print(Id_array)
print(value_array)

plt.plot(value_array)
plt.show()
