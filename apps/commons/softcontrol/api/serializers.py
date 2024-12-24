from rest_framework.serializers import ModelSerializer


class SoftControlModelSerializer(ModelSerializer):

    def create(self, validated_data):

        request = self.context['request']

        # SoftControlModel
        validated_data['created_user'] = request.user
        validated_data['updated_user'] = request.user

        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        request = self.context['request']

        # SoftControlModel
        validated_data['updated_user'] = request.user

        instance = super().update(instance, validated_data)
        return instance
