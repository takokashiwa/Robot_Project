from roboter.models import robot
from roboter.models import ranking_model 

robot = robot.Robot()
ranking_model = ranking_model.RankingModel()
robot.hello()
ranking_model.register_csv()
