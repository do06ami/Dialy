from diaries.AbstractDiary import AbstractDiary

class NagataniDiary2(AbstractDiary):
    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "明日はいい日。"
    def get_author(self):
        return "Nagatani2"