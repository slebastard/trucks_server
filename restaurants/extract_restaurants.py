 def extract_users():
        """
        This will extract users:
            - who began their first cesure more than eight months ago,
            - who are after their 2A and before their graduation,
            - who have not already received a mail about the cesure
        """
        # We choose the users having done a first cesure
        have_xp = []
        for xp in Experience.objects.filter(experience_type='16').filter(start_date__month=start_month):
            have_xp.append(xp.linked_profile.id)
        users = User.objects.filter(id__in=have_xp)

        return users \
            .exclude(profile__promo__gte=promo_2A) \
            .exclude(profile__promo__lt=graduated) \
            .exclude(emails_sent__mailtype="cesureSecondPart") \


    @staticmethod
    def process(user):

        mailtype = 'cesureSecondPart'
        sender = "Mickaël Bergem <mickael.bergem@ponts.org>"

        return {
            'subject': "Comment se passe ta deuxième partie de césure?",
            'to': user.email,
            'context_dict': {'user': user},
            'email_template': "{}.txt".format(mailtype),
            'from_addr': sender,
        }, mailtype
