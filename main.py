from  Review import  Review, Reviews
request_url = "https://play.google.com/store/apps/details?id=com.nexon.kart&showAllReviews=true"

def _main() :
    review = Reviews(request_url)
    review.getReviews(review.url)
    # for i in review.reviews :
        # print("데이터 개수 : ", len(review.reviews))
        # print(i.stars,"점 - ", i.date, i.comment, )

if __name__ == "__main__":
    _main()
