import factory
import faker
from survey_app.surveys.models import StorySurvey

fake = faker.Faker()


class StorySurveyFactory(factory.DjangoModelFactory):
    title = factory.LazyAttribute(lambda n: fake.sentence(
        nb_words=6,
        variable_nb_words=True
    ))
    is_public = True
    start = factory.LazyAttribute(lambda n: fake.paragraph())
    end = factory.LazyAttribute(lambda n: fake.paragraph())

    class Meta:
        model = StorySurvey
