from django.contrib.auth.models import User
from translation.models import TranslateOrigin
from profiles.models import Project, LanguageText
from tqdm import tqdm



with open('./malayalam.txt') as f:
    project = Project.objects.get(pk=1)
    language, _ = LanguageText.objects.get_or_create(language='ml')
    for line in tqdm(f):
        # print(line)
        _, created = TranslateOrigin.objects.get_or_create(
            project_name=project,
            language=language,
            text=line.rstrip('\n'),
            )
