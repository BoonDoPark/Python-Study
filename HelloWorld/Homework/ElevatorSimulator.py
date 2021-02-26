import datetime
import random
from typing import List


class Elevator:
    def __init__(self):
        self.current_floor = random.randint(1, 20)

    def move(self, destination_floor):
        self.current_floor = destination_floor


class ElevatorScheduler:
    def __init__(self):
        pass

    def get_current_datetime(self):
        """
        2021.02.26.hsk : 현재 시간 객체(datetime 타입) 반환
        :return:
        """
        # 여기에 로직 추가
        pass

    def compare_between_current_datetime_and_afternoon(self) -> bool:
        """
        2021.02.26.hsk : 현재 시간이 오후인지 아닌지 비교
        :return:
        """
        # 여기에 로직 추가
        pass

    def select_elevator(self, my_floor, elevators: List[Elevator]) -> Elevator:
        """
        2021.02.26.hsk : 현재 시간이 오후인지 알아내고 어떤 엘레베이터를 탈지 결정
        :param my_floor:
        :param elevators:
        :return:
        """
        elevator: Elevator = None
        # 여기에 로직 추가
        return elevator


class Me:
    def __init__(self):
        self.my_floor = random.randint(1, 20)

    def push_up_button(self):
        up_to_floor = int(input('올라갈 층을 입력해.'))
        if up_to_floor > self.my_floor:
            self.my_floor = up_to_floor
        else:
            print('말이 안되')

    def push_down_button(self):
        down_to_floor = int(input('내려갈 층을 입력해.'))
        if down_to_floor < self.my_floor:
            self.my_floor = down_to_floor
        else:
            print('말이 안되')


if __name__ == '__main__':
    me = Me()
    elevators: List[Elevator] = [Elevator(), Elevator()]
    scheduler: ElevatorScheduler = ElevatorScheduler()
