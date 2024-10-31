from rest_framework import views
from rest_framework.response import Response
from django.db.models import Sum, Q
from organisations import models as o_models

class StatsView(views.APIView):

    def get(self, request):
        """
        Retourne les statistiques
        """

        participants = o_models.Participants.objects.filter(isParticipants=True)
        speakers = o_models.Participants.objects.filter(isSpeakers=True)
        etudiants = o_models.Participants.objects.filter(isEtudiants=True)
        presses = o_models.Presses.objects.all()
        organisations = o_models.Organisations.objects.all()

        nbr_participants = participants.count()
        nbr_speakers = speakers.count()
        nbr_etudiants = etudiants.count()
        nbr_organisations = organisations.count() 
        nbr_presses = presses.count() 

        nbr_inscritFJ = o_models.Participants.objects.filter(forumDesJeunes=True).count()
        nbr_inscritFF = o_models.Participants.objects.filter(forumDesFemmes=True).count()
        nbr_inscritFS = o_models.Participants.objects.filter(forumScientifiques=True).count()

        nbr_presentParticipants = participants.filter(estPresent=True).count()
        nbr_presentSpeakers = speakers.filter(estPresent=True).count()
        nbr_presentEtudiants = etudiants.filter(estPresent=True).count()
        nbr_presentOrganisations = organisations.filter(estPresent=True).count()
        nbr_presentPresses = presses.filter(estPresent=True).count()

        nbr_enAttenteParticipants = participants.filter(enAttente=True).count()
        nbr_enAttenteSpeakers = speakers.filter(enAttente=True).count()
        nbr_enAttenteEtudiants = etudiants.filter(enAttente=True).count()
        nbr_enAttenteOrganisations = organisations.filter(enAttente=True).count()
        nbr_enAttentePresses = presses.filter(enAttente=True).count()

        # nbr_nationaleParticipants = participants.filter(provenance=True).count()
        # nbr_nationaleSpeakers = speakers.filter(provenance=True).count()
        # nbr_nationaleEtudiant = etudiants.filter(provenance=True).count()

        nbr_autreDocsParticipants = participants.filter(autreDocument=True).count()
        nbr_autreDocsSpeakers = speakers.filter(autreDocument=True).count()
        nbr_autreDocsEtudiants = etudiants.filter(autreDocument=True).count()

        nbr_lettreParticipants = participants.filter(lettreInvitation=True).count()
        nbr_lettreSpeakers = speakers.filter(lettreInvitation=True).count()
        nbr_lettreEtudiants = etudiants.filter(lettreInvitation=True).count()

        nbr_billetParticipants = participants.filter(priseChargeBillet=True).count()
        nbr_billetSpeakers = speakers.filter(priseChargeBillet=True).count()
        nbr_billetEtudiants = etudiants.filter(priseChargeBillet=True).count()

        nbr_chargeCompleteParticipants = participants.filter(priseChargeComplete=True).count()
        nbr_chargeCompleteSpeakers = speakers.filter(priseChargeComplete=True).count()
        nbr_chargeCompleteEtudiants = etudiants.filter(priseChargeComplete=True).count()

        nbr_hebergementParticipants = participants.filter(priseChargeHebergement=True).count()
        nbr_hebergementSpeakers = speakers.filter(priseChargeHebergement=True).count()
        nbr_hebergementEtudiants = etudiants.filter(priseChargeHebergement=True).count()

        nbr_reservationHotelParticipants = participants.filter(reservationHotel=True).count()
        nbr_reservationHotelSpeakers = speakers.filter(reservationHotel=True).count()
        nbr_reservationHotelEtudiants = etudiants.filter(reservationHotel=True).count()

        nbr_transUrbainParticipants = participants.filter(priseChargetransUrbain=True).count()
        nbr_transUrbainSpeakers = speakers.filter(priseChargetransUrbain=True).count()
        nbr_transUrbainEtudiants = etudiants.filter(priseChargetransUrbain=True).count()

        stats = {}

        stats["nbr_participants"] = nbr_participants
        stats["nbr_speakers"] = nbr_speakers
        stats["nbr_etudiants"] = nbr_etudiants
        stats["nbr_organisations"] = nbr_organisations
        stats["nbr_presses"] = nbr_presses

        stats["nbr_inscritFJ"] = nbr_inscritFJ
        stats["nbr_inscritFF"] = nbr_inscritFF
        stats["nbr_inscritFS"] = nbr_inscritFS

        stats["nbr_presentParticipants"] = nbr_presentParticipants
        stats["nbr_presentSpeakers"] = nbr_presentSpeakers
        stats["nbr_presentEtudiants"] = nbr_presentEtudiants
        stats["nbr_presentOrganisations"] = nbr_presentOrganisations
        stats["nbr_presentPresses"] = nbr_presentPresses

        stats["nbr_enAttenteParticipants"] = nbr_enAttenteParticipants
        stats["nbr_enAttenteSpeakers"] = nbr_enAttenteSpeakers
        stats["nbr_enAttenteEtudiants"] = nbr_enAttenteEtudiants
        stats["nbr_enAttenteOrganisations"] = nbr_enAttenteOrganisations
        stats["nbr_enAttentePresse"] = nbr_enAttentePresses

        # stats["nbr_nationaleParticipants = participants.filter(provenance=True).count()
        # stats["nbr_nationaleSpeakers = speakers.filter(provenance=True).count()
        # stats["nbr_nationaleEtudiant = etudiants.filter(provenance=True).count()

        stats["nbr_autreDocsParticipants"] = nbr_autreDocsParticipants
        stats["nbr_autreDocsSpeakers"] = nbr_autreDocsSpeakers
        stats["nbr_autreDocsEtudiants"] = nbr_autreDocsEtudiants

        stats["nbr_lettreParticipants"] = nbr_lettreParticipants
        stats["nbr_lettreSpeakers"] = nbr_lettreSpeakers
        stats["nbr_lettreEtudiants"] = nbr_lettreEtudiants

        stats["nbr_billetParticipants"] = nbr_billetParticipants
        stats["nbr_billetSpeakers"] = nbr_billetSpeakers
        stats["nbr_billetEtudiants"] = nbr_billetEtudiants

        stats["nbr_chargeCompleteParticipants"] = nbr_chargeCompleteParticipants
        stats["nbr_chargeCompleteSpeakers"] = nbr_chargeCompleteSpeakers
        stats["nbr_chargeCompleteEtudiants"] = nbr_chargeCompleteEtudiants

        stats["nbr_hebergementParticipants"] = nbr_hebergementParticipants
        stats["nbr_hebergementSpeakers"] = nbr_hebergementSpeakers
        stats["nbr_hebergementEtudiants"] = nbr_hebergementEtudiants

        stats["nbr_reservationHotelParticipants"] = nbr_reservationHotelParticipants
        stats["nbr_reservationHotelSpeakers"] = nbr_reservationHotelSpeakers
        stats["nbr_reservationHotelEtudiants"] = nbr_reservationHotelEtudiants

        stats["nbr_transUrbainParticipants"] = nbr_transUrbainParticipants
        stats["nbr_transUrbainSpeakers"] = nbr_transUrbainSpeakers
        stats["nbr_transUrbainEtudiants"] = nbr_transUrbainEtudiants

        stats["nbr_presents"] = nbr_presentParticipants + nbr_presentSpeakers + nbr_presentEtudiants + nbr_presentPresses  + nbr_presentOrganisations -135
        stats["nbr_enAttentes"] = nbr_enAttenteParticipants + nbr_enAttenteSpeakers + nbr_enAttenteEtudiants
        stats["nbr_autreDocs"] = nbr_autreDocsParticipants + nbr_autreDocsSpeakers + nbr_autreDocsEtudiants
        stats["nbr_lettres"] = nbr_lettreParticipants + nbr_lettreSpeakers + nbr_lettreEtudiants
        stats["nbr_chargeCompletes"] = nbr_chargeCompleteParticipants + nbr_chargeCompleteSpeakers + nbr_chargeCompleteEtudiants
        stats["nbr_hebergements"] = nbr_hebergementParticipants + nbr_hebergementSpeakers + nbr_hebergementEtudiants
        stats["nbr_billets"] = nbr_billetParticipants + nbr_billetSpeakers + nbr_billetEtudiants
        stats["nbr_reservationHotels"] = nbr_reservationHotelParticipants + nbr_reservationHotelSpeakers + nbr_reservationHotelEtudiants
        stats["nbr_transUrbains"] = nbr_transUrbainParticipants + nbr_transUrbainSpeakers + nbr_transUrbainEtudiants

        return Response(stats)
