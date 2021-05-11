# 클래스
'''
자동차
    속성:  --> 변수
        번호판, 색상, 속력
    기능:  --> 함수
        경적 울리기, 속력 변경, 오디오
'''

class Car:  # Car 클래스 정의(과자틀, 설계도)
    # 속성(변수)
    num = 0     # 번호
    color = ''  # 색상
    speed = 0   # 속력
    start = ''  # 출발지
    end = ''    # 도착지

    total = 0   # 총 생산대수

    # 기능(함수, 메서드)
    def __init__(self, num, color): # 생성자 메서드(자동차 생성시 자동으로 실행)
        self.num = num      # 번호판 장착
        self.color = color  # 페인트 도색
        self.speed = 0

        Car.total += 1  # Car.total = Car.total + 1 와 동일

        print(f"{num} {color} 자동차가 생산되었습니다. (총 생산대수: {Car.total})")

    def navi(self, start, end):
        self.start = start
        self.end = end
        print(f"{self.num} 이(가) {start} 에서 {end} 로 주행합니다.")

        url = f"https://www.google.com/maps/dir/{start}/{end}"
        print(url)

        import webbrowser
        webbrowser.open(url)

    def horn(self):
        print(f'{self.num} 자동차가 경적을 울립니다.')

    def change_speed(self, v):
        self.speed = self.speed + v
        print(f'{self.num} 속력 변경: {self.speed} km/h')

    def audio(self):
        print(f'{self.num} 오디오 켜기')


'''
버스 특징
    1. 벨 --> 없던 기능 추가
    2. 100 km/h 속력 제한  --> 있던 기능 수정(Over Riding)
'''
class Bus(Car): # Car 부모 클래스를 상속받음
    def bell(self):
        print(f"{self.num} 버스가 벨이 울렸습니다.")

    def change_speed(self, v):
        self.speed = self.speed + v

        # 100km/h 속도 제한 기능 구현
        if self.speed > 100:
            self.speed = 100
        
        print(f'{self.num} 속력 변경: {self.speed} km/h')

# 퀴즈: Car 클래스에 네비게이션 기능 추가해보세요. (출발지, 도착지)

bus1 = Bus(211, 'yellow')
bus1.bell()
bus1.change_speed(50)
bus1.change_speed(50)
bus1.change_speed(50)

car1 = Car(111, 'black')
car1.change_speed(50)
car1.change_speed(50)
car1.change_speed(50)

car2 = Car(113, 'red')
car2.navi('천호역', '부산역')

# car1 = Car(111, 'black')
# car1.bell()

# car1 = Car(111, 'black')
# car1.horn()
# car1.audio()
# car1.change_speed(20)

# car2 = Car(112, 'white')
# car2.horn()
# car2.audio()
# car2.change_speed(10)
# car2.change_speed(10)
# car2.change_speed(-5)


