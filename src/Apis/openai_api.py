from openai import OpenAI
from decouple import config


def getOpenAiClient(OPENAI_API_KEY):
    return OpenAI(
        api_key=OPENAI_API_KEY
    )


class OpenAiModel:
    def __init__(
        self,
        model: str = "gpt-4o-mini",
        api_ky: str = config("OPENAI_API_KEY")
    ) -> None:
        self.client = getOpenAiClient(api_ky)
        self.messages: list[dict[str, str]] = [
            {"role": "system", "content":  "Eres un asistente personal."}
        ]
        self.completeMessages: list[str] = []
        self.files: list = []
        self.model = model
        self.temperature: float = 0

    @staticmethod
    def getOpenAiClient(OPENAI_API_KEY):
        return OpenAI(
            api_key=OPENAI_API_KEY
        )

    def getResponse(self, newUserMessage: str) -> str:
        self.messages.append(
            {
                "role": "user",
                "content": newUserMessage
            }
        )
        completeMessage = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature
        )
        self.completeMessages.append(completeMessage)
        self.messages.append(
            {
                "role": "system",
                "content": completeMessage.choices[0].message.content
            }
        )
        return self.messages[-1]["content"]

    def getStreamResponse(self, newUserMessage: str) -> str:
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": newUserMessage}],
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
