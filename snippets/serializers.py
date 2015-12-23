from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES ,STYLE_CHOICES

'''class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(required=False, allow_blank=True, max_length=100)
    codigo = serializers.CharField(style={'base_template' : 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    linguagem = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    estilo = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """

        create and return a new  'Snippet' instance , given the validate data.
        """

        return  Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Atualiza e retorna  uma instancia de snippet existente , passando a validated_data

        """

        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.linguagem = validated_data.get('linguagem', instance.linguagem)
        instance.estilo = validated_data.get('estilo', instance.estilo)
        instance.save()
        return instance
    '''
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fileds = ('id','titulo','codigo','linenos','linguagem','estilo')
