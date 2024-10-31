from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from backend.settings import EMAIL_HOST_USER
import base64
from email.mime.base import MIMEBase
from email import encoders
from django.core.mail import EmailMultiAlternatives
import os
import magic
from backend.settings import BASE_DIR
from weasyprint import HTML
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from io import BytesIO

#***************************** ModelViewSets********************************

class ParticipantsModelViewSet(ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class=serializers.ParticipantsSerializer
    def get_queryset(self):
        return models.Participants.objects.all().order_by('-created_at')


class OrganisationsModelViewSet(ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class=serializers.OrganisationsSerializer  
    def get_queryset(self):
        return models.Organisations.objects.all().order_by('-created_at')
    
    
class PressesModelViewSet(ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class=serializers.PressesSerializer  
    def get_queryset(self):
        return models.Presses.objects.all().order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)

        presses_data = [
            {
                'id': presse['id'],
                'reference': presse['reference'],
                'civilite': presse['civilite'],
                'nom': presse['nom'],
                'prenom': presse['prenom'],
		'deuxiemeprenom': presse['deuxiemeprenom'],
                'organePresse': presse['organePresse'],
                'email': presse['email'],
                'telephone': presse['telephone'],
                'estPresent': presse['estPresent'],
                'enAttente': presse['enAttente'],
                'autreDocument': presse['autreDocument'],
                'priseChargeBillet': presse['priseChargeBillet'],
                'priseChargeComplete': presse['priseChargeComplete'],
                'priseChargeHebergement': presse['priseChargeHebergement'],
                'reservationHotel': presse['reservationHotel'],
            }
            for presse in serializer.data
        ]

        return Response(presses_data)
    

class ParticipantsSimpleView(APIView):
    def get(self, request):
        data = models.Participants.objects.filter(isParticipants=True).order_by('-created_at')
        serializer = serializers.ParticipantsSerializer(data, many=True)
        participants_data = [
            {
                'id': participant['id'],
                'reference' : participant['reference'],
                'civilite': participant['civilite'],
                'nom': participant['nom'],
                'prenom': participant['prenom'],
		'deuxiemeprenom': participant['deuxiemeprenom'],
		'organisme': participant['organisme'],
                'fonction': participant['fonction'],
                'email1': participant['email1'],
                'telephone': participant['telephone'],
                'estPresent': participant['estPresent'],
                'enAttente': participant['enAttente'],
                'forumDesJeunes': participant['forumDesJeunes'],
                'forumDesFemmes': participant['forumDesFemmes'],
                'forumScientifiques': participant['forumScientifiques'],
                'autreDocument': participant['autreDocument'],
                'lettreInvitation': participant['lettreInvitation'],
                'priseChargeBillet': participant['priseChargeBillet'],
                'priseChargeComplete': participant['priseChargeComplete'],
                'priseChargeHebergement': participant['priseChargeHebergement'],
                'reservationHotel': participant['reservationHotel'],
                'priseChargetransUrbain': participant['priseChargetransUrbain'],
            }

            for participant in serializer.data
        ]
        
        return Response(participants_data)


class SpeakersView(APIView):
    def get(self, request):
        data = models.Participants.objects.filter(isSpeakers=True).order_by('-created_at')
        serializer = serializers.ParticipantsSerializer(data, many=True)
        speakers_data = [
            {
                'id': speaker['id'],
		'reference': speaker['reference'],
                'civilite': speaker['civilite'],
                'nom': speaker['nom'],
                'prenom': speaker['prenom'],
		'deuxiemeprenom': speaker['deuxiemeprenom'],
		'organisme': speaker['organisme'],
                'fonction': speaker['fonction'],
                'email1': speaker['email1'],
                'telephone': speaker['telephone'],
                'estPresent': speaker['estPresent'],
                'enAttente': speaker['enAttente'],
                'forumDesJeunes': speaker['forumDesJeunes'],
                'forumDesFemmes': speaker['forumDesFemmes'],
                'forumScientifiques': speaker['forumScientifiques'],
                'autreDocument': speaker['autreDocument'],
                'lettreInvitation': speaker['lettreInvitation'],
                'priseChargeBillet': speaker['priseChargeBillet'],
                'priseChargeComplete': speaker['priseChargeComplete'],
                'priseChargeHebergement': speaker['priseChargeHebergement'],
                'reservationHotel': speaker['reservationHotel'],
                'priseChargetransUrbain': speaker['priseChargetransUrbain'],
            }

            for speaker in serializer.data
        ]

        return Response(speakers_data)


class EtudiantsView(APIView):
    def get(self, request):
        data = models.Participants.objects.filter(isEtudiants=True).order_by('-created_at')
        serializer = serializers.ParticipantsSerializer(data, many=True)
        etudiants_data = [
            {
                'id': etudiant['id'],
		'reference': etudiant['reference'],
                'civilite': etudiant['civilite'],
                'nom': etudiant['nom'],
                'prenom': etudiant['prenom'],
		'deuxiemeprenom': etudiant['deuxiemeprenom'],
                'organisme': etudiant['organisme'],
                'fonction': etudiant['fonction'],
                'email1': etudiant['email1'],
                'telephone': etudiant['telephone'],
                'estPresent': etudiant['estPresent'],
                'enAttente': etudiant['enAttente'],
                'forumDesJeunes': etudiant['forumDesJeunes'],
                'forumDesFemmes': etudiant['forumDesFemmes'],
                'forumScientifiques': etudiant['forumScientifiques'],
                'autreDocument': etudiant['autreDocument'],
                'lettreInvitation': etudiant['lettreInvitation'],
                'priseChargeBillet': etudiant['priseChargeBillet'],
                'priseChargeComplete': etudiant['priseChargeComplete'],
                'priseChargeHebergement': etudiant['priseChargeHebergement'],
                'reservationHotel': etudiant['reservationHotel'],
                'priseChargetransUrbain': etudiant['priseChargetransUrbain'],
            }

            for etudiant in serializer.data
        ]

        return Response(etudiants_data)


class InscritsView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reference = request.data.get('reference')
        if not reference:
            return Response({'message': "Reference is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Try to find the participant
        try:
            participant = get_object_or_404(models.Participants, reference=reference)
            serializer = serializers.ParticipantsSerializer(participant)
            return Response(serializer.data)
        except:
            pass

        # Try to find the organisation
        try:
            organisation = get_object_or_404(models.Organisations, reference=reference)
            serializer = serializers.OrganisationsSerializer  (organisation)
            return Response(serializer.data)
        except:
            pass

        # Try to find the press
        try:
            press = get_object_or_404(models.Presses, reference=reference)
            serializer = serializers.PressesSerializer (press)
            return Response(serializer.data)
        except:
            pass

        return Response({'message': "Données introuvable"}, status=status.HTTP_404_NOT_FOUND)


class VerifieView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        data = request.data
        reference = None
        data_find = {}
        data_find['find']= False
        try:
            reference = data['reference']
        except:
            return Response({'message': "Reference is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        participant = models.Participants.objects.filter(reference=reference).first()
        if not participant:
            participant = models.Organisations.objects.filter(reference=reference).first()
        if not participant:
            participant = models.Presses.objects.filter(reference=reference).first()
        if participant:
        # Update enAttente attribute
            participant.estPresent = True
            participant.save()
            data_find['find'] = True
            
        return Response(data_find)
        

class ConfirmationsView(APIView):
    def post(self, request):
        data = request.data
        badge = data.get('badge')
        type_participant = data.get('type')
        id_participant = data.get('id')

        if not badge:
            return Response({'message': "Badge is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        if not type_participant:
            return Response({'message': "Type is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not id_participant:
            return Response({'message': "Id is required"}, status=status.HTTP_400_BAD_REQUEST)
        print(id,' ',type,)
        participant = self.get_participant(id_participant, type_participant)

        if not participant:
            return Response({'message': "Demandeur introuvable"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not participant.enAttente:
            return Response({'message': "Déjà confirmé"}, status=status.HTTP_400_BAD_REQUEST)

        allowed_types = {"participant", "speaker", "etudiant"}
        fonction = None
        structure = None
        if type_participant in allowed_types:
            fonction = participant.fonction
            structure = participant.organisme
        elif type_participant == "organisation":
            fonction = "Membre d'organisation" if participant.lang == "Fr" else "Organization Member"
            structure = participant.commission
        else:
            fonction = "Presse" if participant.lang == "Fr" else "Press"
            structure = participant.organePresse
        reference = participant.reference

        context = {
            'prenom_nom': f"{participant.civilite} {participant.prenom.title()} {participant.nom.title()}",
            'fonction': fonction,
            'structure': structure,
            'civilite': participant.civilite,
            'reference': reference
        }

        html_string = None
        if type_participant == "speaker":
            html_string = render_to_string('invitation_speakers_fr.html', context) if participant.lang == "Fr" else render_to_string('invitation_speakers_en.html', context)
        else:
            html_string = render_to_string('invitation_participants_fr.html', context) if participant.lang == "Fr" else render_to_string('invitation_participants_en.html', context)

        invitation_file = BytesIO()
        HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf(invitation_file)
        invitation_file.seek(0)

        email = getattr(participant, 'email', None) or getattr(participant, 'email1', None)
        email2 = getattr(participant, 'email2', None)

        agenda_file = 'agenda_EN.pdf' if participant.lang == "En" else 'agenda_FR.pdf'
        note_file = 'NOTE_CONCEPTUELLE_EN.pdf' if participant.lang == "En" else 'NOTE_CONCEPTUELLE_FR.pdf' 
        
        agenda_path = os.path.join(settings.MEDIA_ROOT, agenda_file)
        note_path = os.path.join(settings.MEDIA_ROOT, note_file)

        subject = "Confirmation inscription" if participant.lang == "Fr" else "Registration confirmation"
        email_body = render_to_string('email_body_fr.html', context) if participant.lang == "Fr" else render_to_string('email_body_en.html', context)
        recipient_list = [email] if not email2 else [email, email2]

        message = EmailMultiAlternatives(
            subject, 
            email_body, 
            settings.EMAIL_HOST_USER, 
            recipient_list
        )

        badge_file = BytesIO(base64.b64decode(badge))
        message.attach("badge.png", badge_file.read(), 'application/png')

        with open(agenda_path, 'rb') as agenda:
            message.attach("programme synoptique.pdf", agenda.read(), 'application/pdf') if participant.lang == "Fr" else message.attach("synotic agenda.pdf", agenda.read(), 'application/pdf')

        with open(note_path, 'rb') as note:
            message.attach("note conceptuelle.pdf", note.read(), 'application/pdf') if participant.lang == "Fr" else message.attach("concept note.pdf", note.read(), 'application/pdf')

        message.attach("invitation.pdf", invitation_file.read(), 'application/pdf')
        message.attach_alternative(email_body, "text/html")
        message.send(fail_silently=False)
        
        participant.enAttente = False
        participant.save()

        return Response({'message': "Participant is confirmed"}, status=status.HTTP_201_CREATED)

    def get_participant(self, id_participant, type_participant):
        model_mapping = {
            "participant": models.Participants,
            "speaker": models.Participants,
            "etudiant": models.Participants,
            "organisation": models.Organisations,
            "presse": models.Presses
        }

        model = model_mapping.get(type_participant)
        if model:
            participant = model.objects.get(id=id_participant)
            if participant:
                return participant
            else:
                participant = None

        return None


class RejetsView(APIView):
    def post(self, request):
        data = request.data
        type_participant = data.get('type')
        id_participant = data.get('id')

        if not type_participant:
            return Response({'message': "Type is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not id_participant:
            return Response({'message': "Id is required"}, status=status.HTTP_400_BAD_REQUEST)
        participant = self.get_participant(id_participant, type_participant)

        if not participant:
            return Response({'message': "Demandeur introuvable"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not participant.enAttente:
            return Response({'message': "Déjà confirmé"}, status=status.HTTP_400_BAD_REQUEST)

        email = getattr(participant, 'email', None) or getattr(participant, 'email1', None)
        email2 = getattr(participant, 'email2', None)

        subject = "Information concernant votre inscription au Forum Galien Afrique 2024" if participant.lang == "Fr" else "Information concerning your registration for the Galien Forum Afrique 2024"
        email_body = render_to_string('email_rejet_fr.html') if participant.lang == "Fr" else render_to_string('email_rejet_en.html')
        recipient_list = [email] if not email2 else [email, email2]

        message = EmailMultiAlternatives(
            subject, 
            email_body, 
            settings.EMAIL_HOST_USER, 
            recipient_list
        )

        message.attach_alternative(email_body, "text/html")
        message.send(fail_silently=False)
        
        participant.delete()

        return Response({'message': "Participant rejected"}, status=status.HTTP_201_CREATED)

    def get_participant(self, id_participant, type_participant):
        model_mapping = {
            "participant": models.Participants,
            "speaker": models.Participants,
            "etudiant": models.Participants,
            "organisation": models.Organisations,
            "presse": models.Presses
        }

        model = model_mapping.get(type_participant)
        if model:
            participant = model.objects.get(id=id_participant)
            if participant:
                return participant
            else:
                participant = None

        return None


class RemercimentsView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        data = request.data
        id = None
        try:
            id = data['id']
        except:
            return Response({'message': "id is required"}, status=status.HTTP_400_BAD_REQUEST)       

        participant = models.Participants.objects.get(id=id)
        forum = "Forum Galien sur le sous-thème ""Maladies non-transmissibles : L'Afrique en lutte !""du 22 au 25 octobre 2024" if participant.lang == "Fr" else  "Galen Forum on the sub-theme ""Non-communicable diseases: Africa in the fight!"" from October 22 to 25, 2024" 

        if participant.forumDesJeunes:
            forum = 'Forum des Jeunes sur le sous-thème "Jeunes et Innovations pour lutter contre les Maladies Non Transmissibles" ce 23 octobre 2024' if participant.lang == "Fr" else 'Youth Forum on the sub-theme "Young people and Innovations to fight Non-Communicable Diseases" this October 23, 2024'

        if participant.forumDesFemmes:
            forum = 'Forum des Femmes "Quelle place pour les femmes dans la lutte contre les Maladies Non Transmissibles en Afrique ?" ce 24 octobre 2024' if participant.lang == "Fr" else 'Women''s Forum "What place for women in the fight against Non-Communicable Diseases in Africa?" this October 24, 2024'
        
        if participant.forumScientifiques:
            forum = 'Forum Scientifique "Rôle de la Multisectorialité dans la prévention des MNT" ce 25 octobre 2024' if participant.lang == "Fr" else 'Scientific Forum "Role of Multisectorality in the prevention of NCDs" this October 25, 2024'

        context = {
            'prenom_nom': f"{participant.civilite} {participant.prenom.title()} {participant.nom.title()}",
            'fonction': participant.fonction,
            'structure': participant.organisme,
            'civilite': participant.civilite,
            'reference': participant.reference,
            'forum': forum
        }
        
        html_string = render_to_string('remerciments_fr.html', context) if participant.lang == "Fr" else render_to_string('remerciments_en.html', context)
        
        remerciment_file = BytesIO()
        HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf(remerciment_file)
        remerciment_file.seek(0)
        
        email2 = getattr(participant, 'email2', None)

        subject = (
            f"Remerciements pour votre participation au panel {forum}" 
            if participant.lang == "Fr" 
            else f"Thanks for your participation in the panel {forum}"
        )         

        recipient_list = [participant.email1] if email2 is None else [participant.email1, email2]

        email_body = render_to_string('remerciments_body_fr.html', context) if participant.lang == "Fr" else render_to_string('remerciments_body_en.html', context)

        message = EmailMultiAlternatives(
            subject,
            email_body,
            settings.EMAIL_HOST_USER,
            recipient_list
        )

        message.attach("remerciment.pdf", remerciment_file.read(), 'application/pdf') if participant.lang == "Fr" else message.attach("Acknowledgments.pdf", remerciment_file.read(), 'application/pdf')
        message.attach_alternative(email_body, "text/html")
        message.send(fail_silently=False)
            
        return Response({'message': "Lettre de remerciments envoyée"}, status=status.HTTP_201_CREATED)
