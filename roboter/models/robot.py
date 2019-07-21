class Robot():
     def __init__(self, user_name = None, favorite_restaurant = None, speaking_color = 'red'):
       self.user_name = user_name 
       self.favorite_restaurant = favorite_restaurant
       self.speaking_color = speaking_color 

     def get_user_name(self):
         return self.user_name 

     def set_user_name(self, user_name):
         self.user_name = user_name

     def get_favorite_restaurant(self):
         return self.favorite_restaurant

     def set_favorite_restaurant(self, favorite_restaurant):
         self.favorite_restaurant = favorite_restaurant

    
     def hello(self):
        print("====================")
        print("こんにちは！私はRobokoです。あなたの名前は何ですか？")
        print("====================")

        self.user_name = input("Please input your name:") 

        print("こんにちは{}さん。どこのレストランが好きですか？".format(self.user_name))

        self.favorite_restaurant = input("Please type your favorite restaurant:")

        print("{}さん。ありがとうございました。".format(self.user_name))
        print("良い一日を！さようなら")

        # return self.user_name 
        # return self.favorite_restaurant