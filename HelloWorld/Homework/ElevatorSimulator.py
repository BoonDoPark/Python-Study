import datetime
import random
from typing import List


class Me:
    def __init__(self):
        self.my_floor = random.randint(1, 20)

    def push_up_button(self):
        destination_up_to_floor = int(input('올라갈 층 숫자를 입력해. {0}층 ~ 20층 : '.format(str(self.my_floor))))
        if destination_up_to_floor < self.my_floor:
            print('잘못입력했어.')
            return
        return destination_up_to_floor

    def push_down_button(self):
        destination_down_to_floor = int(input('내려갈 층 숫자를 입력해. 1층 ~ {0}층 : '.format(str(self.my_floor))))
        if destination_down_to_floor > self.my_floor:
            print('잘못입력했어.')
            return
        return destination_down_to_floor

    def move(self, destination_floor):
        self.my_floor = destination_floor


class Elevator:
    def __init__(self):
        self.current_floor = random.randint(1, 20)

    def move(self, destination_floor):
        self.current_floor = destination_floor
        return True


class ElevatorScheduler:
    def __init__(self, elevators: List[Elevator]):
        self.elevators = elevators

    def get_current_datetime(self):
        """
        2021.02.26.hsk : 현재 시간 객체(datetime 타입) 반환
        :return:
        """
        # 여기에 로직 추가
        pass

    def is_current_datetime_afternoon(self) -> bool:
        """
        2021.02.26.hsk : 현재 시간이 오후인지 아닌지 비교
        :return:
        """
        # 여기에 로직 추가
        pass

    def select_elevator(self, my_floor) -> int:
        """
        2021.02.26.hsk : 현재 시간이 오후인지 알아내고 몇번 엘레베이터를 탈지 결정
        - 오전일 경우 나와 가까운 엘레베이터 선택
        - 오후일 경우 나와 멀리있는 엘레베이터 선택
        :param my_floor: 현재 내가 있는 층
        :return:
        """
        selected_elevator_num = -1  # 선택된 엘레베이터 번호 (0번째, 1번째) / -1일경우 선택이 안된 상태
        # 오전 오후 구글링, 오전 :
        # 여기에 로직 추가
        # 1.get_current_datetime 얻어오기 다음에 반환
        # 2.is_current_datetime_afternoon if문 분기
        # 3.for문 self.elevators 층, elevator.current_floor, my_floor 비교(elevator.current_floor - my_floor), abs함수이용
        # 오전. 크기작음, 오후. 크기큼, enumerate->select_elevator, idx값을 할당 순서 주의

        return selected_elevator_num


class Simulator:
    def __init__(self):
        self.me = Me()
        self.elevators = [Elevator(), Elevator()]
        self.scheduler = ElevatorScheduler(self.elevators)
        self.show_current_floor()

    def show_current_floor(self):
        """
        2021.02.26.hsk : 현재 상태 (몇층인지) 출력
        :return:
        """
        print('나 : {0}층'.format(self.me.my_floor))
        for index, elevator in enumerate(self.elevators):
            print('{0}번 엘레베이터 : {1}층'.format(index, elevator.current_floor))
        print('\n')

    def question_to_me(self, up_or_down):
        destination_floor = None
        if up_or_down == 'U':
            destination_floor = self.me.push_up_button()
        elif up_or_down == 'D':
            destination_floor = self.me.push_down_button()
        return destination_floor

    def process(self):
        while True:
            # 내려갈지 올라갈지 선택
            up_or_down = input('올라갈까? 내려갈까? (U/D) : ')

            # 목표하는 층을 얻어냄
            destination_floor = self.question_to_me(up_or_down)
            if not destination_floor:
                break

            # 스케줄러에 의해 몇번 엘레베이터가 움직일지 정해짐
            selected_elevator_num = self.scheduler.select_elevator(self.me.my_floor)
            selected_elevator = self.elevators[selected_elevator_num]

            # 선택된 엘레베이터가 이동하면 나도 이동함
            if selected_elevator.move(destination_floor):
                self.me.move(destination_floor)

            # 현재 층 상태를 보여줌
            self.show_current_floor()


if __name__ == '__main__':
    simulator = Simulator()
    simulator.process()
