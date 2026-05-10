# from transformers import pipeline

# # Load summarization pipeline
# summarizer = pipeline(
#     "summarization",
#     model="facebook/bart-large-cnn"
# )

# def generate_summary(text):

#     if len(text.strip()) == 0:
#         return "Empty text provided."

#     try:
#         summary = summarizer(
#             text,
#             max_length=130,
#             min_length=30,
#             do_sample=False
#         )

#         return summary[0]['summary_text']

#     except Exception as e:
#         return f"Error: {str(e)}"

# from transformers import pipeline

# summarizer = pipeline(
#     "summarization",
#     model="facebook/bart-large-cnn"
# )

# def generate_summary(text):

#     summary = summarizer(
#         text,
#         max_length=130,
#         min_length=30,
#         do_sample=False
#     )

#     return summary[0]['summary_text']
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def generate_summary(text):

    input_length = len(text.split())

    # Dynamic max/min length
    max_len = min(130, input_length // 2)

    min_len = min(30, max_len - 5)

    # Prevent very small values
    if max_len < 20:
        max_len = 20

    if min_len < 5:
        min_len = 5

    summary = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return summary[0]['summary_text']