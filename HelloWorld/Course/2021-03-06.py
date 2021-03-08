import datetime
import random
from typing import List


class Me:
    def __init__(self):
        max_floor = Simulator.get_max_floor()
        min_floor = Simulator.get_min_floor()
        self.my_floor = random.randint(min_floor, max_floor)

    def push_up_button(self):
        """
        2021.02.26.hsk : 위로 올라가는 버튼 클릭
        :return:
        """
        destination_up_to_floor = int(input('올라갈 층 숫자를 입력해. {0}층 ~ 20층 : '.format(str(self.my_floor))))
        if destination_up_to_floor < self.my_floor:
            print('잘못입력했어.')
            return
        return destination_up_to_floor

    def push_down_button(self):
        """
        2021.02.26.hsk : 아래로 내려가는 버튼 클릭
        :return:
        """
        destination_down_to_floor = int(input('내려갈 층 숫자를 입력해. 1층 ~ {0}층 : '.format(str(self.my_floor))))
        if destination_down_to_floor > self.my_floor:
            print('잘못입력했어.')
            return
        return destination_down_to_floor

    def move(self, destination_floor):
        """
        2021.02.26.hsk : 나 자신이 목표층으로 이동
        :param destination_floor: 목표층
        :return:
        """
        self.my_floor = destination_floor


class Elevator:
    def __init__(self):
        max_floor = Simulator.get_max_floor()
        min_floor = Simulator.get_min_floor()
        self.current_floor = random.randint(min_floor, max_floor)

    def move(self, destination_floor):
        """
        2021.02.26.hsk : 엘레베이터 이동
        :param destination_floor: 목표층
        :return:
        """
        self.current_floor = destination_floor
        return True


class ElevatorScheduler:
    def __init__(self, elevators: List[Elevator]):
        self.elevators = elevators

    @staticmethod
    def _get_current_datetime():
        """
        2021.02.26.hsk : 현재 시간 객체(datetime 타입) 반환
        :return:
        """
        # 여기에 로직 추가
        return datetime.datetime.now()

    @staticmethod
    def _is_current_datetime_afternoon(current_datetime) -> bool:
        """
        2021.02.26.hsk : 현재 시간이 오후인지 아닌지 비교 (오후일 경우 True, 오전일 경우 False 리턴)
        :param current_datetime: 현재 시간 datetime 객체
        :return:
        """
        # 여기에 로직 추가
        is_am_pm = current_datetime.strftime('%p')
        if is_am_pm == 'PM':
            return True
        elif is_am_pm == 'AM':
            return False

    def select_elevator(self, my_floor) -> int:
        """
        2021.02.26.hsk : 현재 시간이 오후인지 알아내고 몇번 엘레베이터를 탈지 결정
        - 오전일 경우 나와 가까운 엘레베이터 선택
        - 오후일 경우 나와 멀리있는 엘레베이터 선택
        :param my_floor: 현재 내가 있는 층
        :return:
        """
        selected_elevator_num = -1  # 선택된 엘레베이터 번호 (0번째, 1번째) / -1일경우 선택이 안된 상태

        # 여기에 로직 추가 (아래의 순서대로 로직을 구현할 것)
        # 1. get_current_datetime 구현 :  현재 시간 얻어오기 (current_datetime 변수 선언 후 현재시간 datetime 객체 할당)
        # 2. is_current_datetime_afternoon 구현 : 함수 주석 참고
        # 3-1. for, enumerate 을 통해 self.elevators 순회
        # 3-2.for 문 내부에서 is_current_datetime_afternoon 의 결과에 따라 if 문으로 분기
        # 3-3. my_floor 와 elevator.current_floor 비교
        # 3-3. 두 값의 차에 abs 함수 사용 (절대값)
        # 3-4. 적합한 index 값을 selected_elevator_num 에 할당.
        current_datetime = self._get_current_datetime()
        is_afternoon = self._is_current_datetime_afternoon(current_datetime)

        min_diff = 20
        max_diff = 0

        for elevator_num, elevator in enumerate(self.elevators):
            distance = abs(my_floor - elevator.current_floor)
            selected_elevator_num = elevator_num
            if is_afternoon:
                if distance > max_diff:
                    max_diff = distance
            else:
                if distance < min_diff:
                    min_diff = distance

        return selected_elevator_num


class Simulator:
    max_floor = 20
    min_floor = 1

    def __init__(self):
        self.me = Me()
        elevator_count = self._set_elevator_count()
        self.elevators = [Elevator() for i in range(elevator_count)]
        self.scheduler = ElevatorScheduler(self.elevators)
        self.show_current_floor()

    @classmethod
    def get_max_floor(cls):
        return cls.max_floor

    @classmethod
    def get_min_floor(cls):
        return cls.min_floor

    @staticmethod
    def _set_elevator_count():
        """
        2021.02.26.hsk : 엘레베이터 갯수 초기화
        :return:
        """
        elevator_count = int(input('엘레베이터 갯수는 몇개로 할까? : '))
        print('\n')
        return elevator_count

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
        """
        2021.02.26.hsk : 나 자신으로부터 목적지를 얻어내기
        :param up_or_down:
        :return:
        """
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
