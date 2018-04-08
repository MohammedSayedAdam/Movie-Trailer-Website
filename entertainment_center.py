import fresh_tomatoes
import media
finding_nemo = media.movie(
                           "Finding Nemo",
                           "finding nemo.jpeg",
                           "https://www.youtube.com/watch?v=2zLkasScy7A"
                           )
school_of_rock = media.movie(
                             "School Of Rock",
                             "School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc"
                             )
hermano = media.movie(
                      "Hermano",
                      "hemano.jpg",
                      "https://www.youtube.com/watch?v=5vrrRJDN64U"
                      )
movies_list = [finding_nemo, school_of_rock, hermano]
fresh_tomatoes.open_movies_page(movies_list)
