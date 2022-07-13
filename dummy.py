import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

data='Thomas Cruise Mapother IV (born July 3, 1962) is an American actor and producer. One of the world\'s highest-paid actors,[1] he has received various accolades, including an Honorary Palme d\'Or and three Golden Globe Awards, in addition to nominations for three Academy Awards. His films have grossed over $4 billion in North America and over $10.1 billion worldwide,[2] making him one of the highest-grossing box office stars of all time.[3]Cruise began acting in the early 1980s and made his breakthrough with leading roles in the comedy film Risky Business (1983) and action film Top Gun (1986). Critical acclaim came with his roles in the dramas The Color of Money (1986), Rain Man (1988), and Born on the Fourth of July (1989). For his portrayal of Ron Kovic in the latter, he won a Golden Globe Award and received a nomination for the Academy Award for Best Actor. As a leading Hollywood star in the 1990s, he starred in several commercially successful films, including the drama A Few Good Men (1992), the thriller The Firm (1993), the horror film Interview with the Vampire (1994), and the romance Jerry Maguire (1996). For the latter, he won a Golden Globe Award for Best Actor and received his second Academy Award nomination. Cruise\'s performance as a motivational speaker in the drama Magnolia (1999) earned him another Golden Globe Award and a nomination for the Academy Award for Best Supporting Actor.Since then, Cruise has largely starred in science fiction and action films, establishing himself as an action star, often performing his own risky stunts. He has played Ethan Hunt in all six of the Mission: Impossible films from 1996 to 2018. His other notable roles in the genre include Vanilla Sky (2001), Minority Report (2002), The Last Samurai (2003), Collateral (2004), War of the Worlds (2005), Knight and Day (2010), Jack Reacher (2012), Oblivion (2013), Edge of Tomorrow (2014), and Top Gun: Maverick (2022). The last of these ranks as his highest-grossing release.Cruise has been married to actresses Mimi Rogers, Nicole Kidman, and Katie Holmes. He has three children, two of whom were adopted during his marriage to Kidman and the other of whom is a biological daughter he had with Holmes. Cruise is an outspoken advocate for the Church of Scientology, which he credits with helping him overcome dyslexia. In the 2000s, he sparked controversy with his Scientology-affiliated criticisms of psychiatry and anti-depressant drugs, his efforts to promote Scientology in Europe, and a leaked video interview of him promoting Scientology.'

minL=int(input())
maxL=int(input())

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": data,
    "parameters":{"min_length":minL,"max_length":maxL},
})

print(output)