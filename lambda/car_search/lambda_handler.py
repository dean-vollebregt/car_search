

def lambda_handler(event, context):

    from search.search_functions import search_exact_match, search_similar_match

    try:
        if event["operation"] == "search_exact_match":
            return search_exact_match(event)

        if event["operation"] == "search_similar_match":
            return search_similar_match(event)
        else:
            print("Operation not found")

    except Exception as error:
        print('Error processing event: ', error)