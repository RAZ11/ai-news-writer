from app.graph.workflow import graph

from pprint import pprint

result = graph.invoke(
    {
        "topic": "India GDP Growth Outlook"
    }
)

# print(result["final_article"])

print("\n" + "="*80)
print("FINAL ARTICLE")
print("="*80)


article = result["final_article"]

print(f"{article}")



#pprint(result)