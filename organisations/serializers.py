from rest_framework import serializers
from . import models

#**********************Creation des serialiseurs******************#


# #serialiseur table Forums
# class ForumsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Forums
#         fields = "__all__"


#serialiseur table Participants
class ParticipantsSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.Participants
        fields = '__all__'

    def get_type(self, obj):
        if obj.isSpeakers:
            return "speaker"
        elif obj.isEtudiants:
            return "etudiant"
        return "participant"


#serialiseur table Organisations
class OrganisationsSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.Organisations
        fields = '__all__'

    def get_type(self, obj):
        return "organisation"


#serialiseur table Presse
class PressesSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.Presses
        fields = '__all__'

    def get_type(self, obj):
        return "presse"
# #serialiseur table Speakers
# class SpeackersSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Speakers
#         fields = "__all__"


# #serialiseur table Etudiants
# class EtudiantsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Etudiants
#         fields = "__all__"


# #serialiseur table Presses
# class PressesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Presses
#         fields = "__all__"


# #serialiseur table Organisations
# class OrganisationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Organisations
#         fields = "__all__"


# #serialiseur table Evenements
# class EvenementssSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Evenements
#         fields = "__all__"