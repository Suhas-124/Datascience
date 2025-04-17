from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """
The Royal Challengers Bangalore (RCB) is one of the most popular and passionately supported teams in the Indian Premier League (IPL). Based in Bengaluru, RCB is known for its star-studded lineups over the years, including legends like Virat Kohli, AB de Villiers, and Chris Gayle. Despite their massive fan base and powerful squads, RCB has often been labeled as underachievers, yet they continue to fight with resilience and flair. Their matches are packed with excitement, and their signature red and gold jerseys symbolize the energy and spirit they bring to the game. 
Every season, RCB fans chant, “Ee Sala Cup Namde!
Royal Challengers Bangalore (RCB) is a dynamic IPL team that thrives on passion, power, and perseverance. Representing the vibrant city of Bengaluru, RCB has built a legacy of thrilling cricket and loyal fandom. Known for their explosive batting lineups and nail-biting finishes, the team has delivered unforgettable moments, even if the trophy remains elusive. With legends like Kohli leading the charge for years, RCB’s journey is a blend of fire and flair. 
Their fan base, among the most spirited in the league, continues to dream big each season, making “Play Bold” not just a slogan, but a way of life.
"""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''


)

result = splitter.split_text(text)

# print(result)

## using document

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)

print(result[0].page_content)

