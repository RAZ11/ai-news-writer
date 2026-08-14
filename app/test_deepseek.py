
# test_deepseek.py

from services.bedrock_services import generate_article
print("Deep Seek")

response = generate_article(
    "Write a short business news headline about AI."
)

print(response)