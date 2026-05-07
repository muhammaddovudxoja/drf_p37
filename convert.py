import json

with open('convert.json', encoding='utf-16') as f:
    data = json.load(f)

result = [
    {
        "model": "apps.user",
        "pk": item['id'],
        "fields": {
            "name": item["name"],
            "username": item["username"],
            "email": item["email"],
            "phone": item["phone"],
            "website": item["website"],
            "address": item["address"],
            "company": item["company"],
            }
        }
    for item in data
]

with open('apps/fixtures/users.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("✅ SUCCESS")
