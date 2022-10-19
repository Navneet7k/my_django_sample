from rest_framework import serializers

from models import LotteryNew
from .models import LotteryData
class TodoSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Todo
    #     fields = ["task", "completed", "timestamp", "updated", "user"]
    class Meta:
        model = LotteryData
        fields = ["filename", "lottery_name", "first_prize", "second_prize", "third_prize"]

class LotterySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LotteryNew
        fields = ["name", "date", "link"]