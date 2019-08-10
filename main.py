from roboter.models import robot
from roboter.models import ranking_model 

robot = robot.Robot()
ranking_model = ranking_model.RankingModel()
robot.ask_user_name()
robot.ask_favorite_resutaurant()
robot.goob_bye()
#ranking_model.register_csv()
