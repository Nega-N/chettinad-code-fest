from ddgs import DDGS

results = DDGS().text(
    "Dentists in Austin",
    max_results=10
)

print(list(results))