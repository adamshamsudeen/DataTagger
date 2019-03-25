from django.contrib.auth.models import User
from translation.models import TranslateOrigin
from profiles.models import Project, LanguageText
import tqdm



with open('./malaylam.txt') as f:
    for line in tqdm(f):
        project = Project.objects.get(pk=1)
        language = LanguageText.objects.get_or_create(language='ml')
        _, created = TranslateOrigin.objects.get_or_create(
            project_name=project,
            language=language,
            text=line.rstrip('\n'),
            )
