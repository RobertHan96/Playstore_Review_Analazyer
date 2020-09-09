from  Review import  Review, Reviews
request_url = "https://play.google.com/store/apps/details?id=com.nexon.kart&showAllReviews=true"

def _main() :
    review = Reviews(request_url)
    print(review.getReviews(review.url))

if __name__ == "__main__":
    _main()
