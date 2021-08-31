from chatterbot.trainers import ChatterBotCorpusTrainer

from chatterbot import ChatBot
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import LevenshteinDistance

chatbot = ChatBot(
    "My ChatterBot",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": LevenshteinDistance,
            "response_selection_method": get_first_response
        }
    ],
    storage_adapter="chatterbot.storage.SQLStorageAdapter"
)



# trainer = ChatterBotCorpusTrainer(chatbot)
#
# trainer.train(
#     "chatterbot.corpus.english"
# )
