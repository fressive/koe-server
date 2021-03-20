from api.query.artist import Artist
from model.media import Artist as ArtistM

import graphene

class CreateArtist(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        country = graphene.String(default_value="UNKNOWN")
        aliases = graphene.List(graphene.String, default_value=[])

    ok = graphene.Boolean()
    artist = graphene.Field(lambda: Artist)

    @staticmethod
    def mutate(root, info, name, country, aliases):
        model = ArtistM(name=name, country=country, aliases=aliases)
        model.save()

        artist = model
        ok = True
        return CreateArtist(artist=artist, ok=ok)
