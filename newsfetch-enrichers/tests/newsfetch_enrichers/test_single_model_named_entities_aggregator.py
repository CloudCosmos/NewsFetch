import pytest

from common.datatypes import Entity
from newsfetch_enrichers.entity_composer import EntityComposer_Transformers_BI_Strategy
from newsfetch_enrichers.named_entities_aggregator import SingleModelNamedEntitiesAggregator


def test_single_model_aggregator_entity_aggregates_1():
    single_model_aggregator = SingleModelNamedEntitiesAggregator()

    entities = [
        {'confidence': 0.95,
         'description': None,
         'end_offset': 72,
         'entity': 'Thursday , 13 January 2022',
         'label': 'DATE',
         'pos_tag': None,
         'start_offset': 47},
        {'confidence': 0.9,
         'description': None,
         'end_offset': 97,
         'entity': 'Glenn Beck',
         'label': 'PERSON',
         'pos_tag': None,
         'start_offset': 87},
        {'confidence': 0.8,
         'description': None,
         'end_offset': 182,
         'entity': 'Glenn Beck',
         'label': 'PERSON',
         'pos_tag': None,
         'start_offset': 172},
        {'confidence': 0.7,
         'description': None,
         'end_offset': 470,
         'entity': 'GLENN BECK',
         'label': 'PERSON',
         'pos_tag': None,
         'start_offset': 460}
    ]

    for entity in entities:
        single_model_aggregator.add(Entity.parse_obj(entity))

    composed_named_entities, entity_aggregates = single_model_aggregator.aggregate()
    assert len(entity_aggregates) == 2
    assert entity_aggregates["thursday , 13 january 2022DATE"].count == 1
    assert entity_aggregates[
               "thursday , 13 january 2022DATE"].entity == "Thursday , 13 January 2022"
    assert entity_aggregates["thursday , 13 january 2022DATE"].confidence == pytest.approx(0.95)
    assert entity_aggregates["glenn beckPERSON"].count == 3
    assert entity_aggregates["glenn beckPERSON"].entity == "Glenn Beck"
    assert entity_aggregates["glenn beckPERSON"].confidence == pytest.approx((0.9 + 0.8 + 0.7)/3)


def test_single_model_aggregator_entity_aggregates_2():
    composer_strategy = EntityComposer_Transformers_BI_Strategy()
    single_model_aggregator = SingleModelNamedEntitiesAggregator(composer_strategy=composer_strategy)
    entities = [Entity(entity='▁New', label='ORG', model_label='I-ORG', description=None, confidence=0.999988317489624,
                       pos_tag=None, start_offset=0, end_offset=3),
                Entity(entity='▁Horizon', label='ORG', model_label='I-ORG', description=None,
                       confidence=0.9999698400497437, pos_tag=None, start_offset=4, end_offset=11),
                Entity(entity='s', label='ORG', model_label='I-ORG', description=None, confidence=0.9999855756759644,
                       pos_tag=None, start_offset=11, end_offset=12),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999388456344604, pos_tag=None, start_offset=20, end_offset=27),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999550580978394, pos_tag=None, start_offset=28, end_offset=32),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9998821020126343,
                       pos_tag=None, start_offset=32, end_offset=33),
                Entity(entity='▁Expedi', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9995811581611633, pos_tag=None, start_offset=115, end_offset=121),
                Entity(entity='tions', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9948052763938904, pos_tag=None, start_offset=121, end_offset=126),
                Entity(entity='▁L', label='LOC', model_label='I-LOC', description=None, confidence=0.9999878406524658,
                       pos_tag=None, start_offset=196, end_offset=197),
                Entity(entity='YON', label='LOC', model_label='I-LOC', description=None, confidence=0.9999880790710449,
                       pos_tag=None, start_offset=197, end_offset=200),
                Entity(entity='▁France', label='LOC', model_label='I-LOC', description=None,
                       confidence=0.9999964237213135, pos_tag=None, start_offset=202, end_offset=208),
                Entity(entity='▁Million', label='ORG', model_label='I-ORG', description=None,
                       confidence=0.9999654293060303, pos_tag=None, start_offset=238, end_offset=245),
                Entity(entity='▁Victor', label='ORG', model_label='I-ORG', description=None,
                       confidence=0.9999769926071167, pos_tag=None, start_offset=246, end_offset=252),
                Entity(entity='ies', label='ORG', model_label='I-ORG', description=None, confidence=0.999975323677063,
                       pos_tag=None, start_offset=252, end_offset=255),
                Entity(entity='▁New', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9998815059661865, pos_tag=None, start_offset=284, end_offset=287),
                Entity(entity='▁Horizon', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.999885082244873, pos_tag=None, start_offset=288, end_offset=295),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9998884201049805,
                       pos_tag=None, start_offset=295, end_offset=296),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9998956918716431, pos_tag=None, start_offset=333, end_offset=340),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999567270278931, pos_tag=None, start_offset=341, end_offset=345),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9998676776885986,
                       pos_tag=None, start_offset=345, end_offset=346),
                Entity(entity='▁iOS', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.5338975787162781, pos_tag=None, start_offset=366, end_offset=369),
                Entity(entity='▁Android', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9465482831001282, pos_tag=None, start_offset=374, end_offset=381),
                Entity(entity='▁New', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9955998659133911, pos_tag=None, start_offset=383, end_offset=386),
                Entity(entity='▁Horizon', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9917435050010681, pos_tag=None, start_offset=387, end_offset=394),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9978440999984741,
                       pos_tag=None, start_offset=394, end_offset=395),
                Entity(entity='▁Expedi', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9993640780448914, pos_tag=None, start_offset=498, end_offset=504),
                Entity(entity='tions', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9951519966125488, pos_tag=None, start_offset=504, end_offset=509),
                Entity(entity='▁RT', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9990197420120239, pos_tag=None, start_offset=575, end_offset=577),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999507665634155, pos_tag=None, start_offset=599, end_offset=606),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999736547470093, pos_tag=None, start_offset=607, end_offset=611),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9998834133148193,
                       pos_tag=None, start_offset=611, end_offset=612),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999475479125977, pos_tag=None, start_offset=626, end_offset=633),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999769926071167, pos_tag=None, start_offset=634, end_offset=638),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9999337196350098,
                       pos_tag=None, start_offset=638, end_offset=639),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999375343322754, pos_tag=None, start_offset=710, end_offset=717),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999713897705078, pos_tag=None, start_offset=718, end_offset=722),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9999152421951294,
                       pos_tag=None, start_offset=722, end_offset=723),
                Entity(entity='▁New', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9996799230575562, pos_tag=None, start_offset=892, end_offset=895),
                Entity(entity='▁Horizon', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9996545314788818, pos_tag=None, start_offset=896, end_offset=903),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9998385906219482,
                       pos_tag=None, start_offset=903, end_offset=904),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999361038208008, pos_tag=None, start_offset=916, end_offset=923),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999715089797974, pos_tag=None, start_offset=924, end_offset=928),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9999158382415771,
                       pos_tag=None, start_offset=928, end_offset=929),
                Entity(entity='▁New', label='ORG', model_label='I-ORG', description=None, confidence=0.9999669790267944,
                       pos_tag=None, start_offset=1077, end_offset=1080),
                Entity(entity='▁Horizon', label='ORG', model_label='I-ORG', description=None,
                       confidence=0.9999256134033203, pos_tag=None, start_offset=1081, end_offset=1088),
                Entity(entity='s', label='ORG', model_label='I-ORG', description=None, confidence=0.9999691247940063,
                       pos_tag=None, start_offset=1088, end_offset=1089),
                Entity(entity='▁Expedi', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9994086027145386, pos_tag=None, start_offset=1287, end_offset=1293),
                Entity(entity='tions', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9967337846755981, pos_tag=None, start_offset=1293, end_offset=1298),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999364614486694, pos_tag=None, start_offset=1343, end_offset=1350),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999741315841675, pos_tag=None, start_offset=1351, end_offset=1355),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9998608827590942,
                       pos_tag=None, start_offset=1355, end_offset=1356),
                Entity(entity='▁Expedi', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9700010418891907, pos_tag=None, start_offset=1358, end_offset=1364),
                Entity(entity='▁Expedi', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9984440207481384, pos_tag=None, start_offset=1615, end_offset=1621),
                Entity(entity='tions', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.8355903625488281, pos_tag=None, start_offset=1621, end_offset=1626),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9998781681060791, pos_tag=None, start_offset=1670, end_offset=1677),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.999956488609314, pos_tag=None, start_offset=1678, end_offset=1682),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.99982750415802,
                       pos_tag=None, start_offset=1682, end_offset=1683),
                Entity(entity='▁New', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999203681945801, pos_tag=None, start_offset=1748, end_offset=1751),
                Entity(entity='▁Horizon', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999125003814697, pos_tag=None, start_offset=1752, end_offset=1759),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9997797608375549,
                       pos_tag=None, start_offset=1759, end_offset=1760),
                Entity(entity='▁Ben', label='PERSON', model_label='I-PER', description=None,
                       confidence=0.9999897480010986, pos_tag=None, start_offset=1889, end_offset=1892),
                Entity(entity='o', label='PERSON', model_label='I-PER', description=None, confidence=0.999975323677063,
                       pos_tag=None, start_offset=1892, end_offset=1893),
                Entity(entity='it', label='PERSON', model_label='I-PER', description=None,
                       confidence=0.9999884366989136, pos_tag=None, start_offset=1893, end_offset=1895),
                Entity(entity='▁Du', label='PERSON', model_label='I-PER', description=None,
                       confidence=0.9999834299087524, pos_tag=None, start_offset=1896, end_offset=1898),
                Entity(entity='cre', label='PERSON', model_label='I-PER', description=None,
                       confidence=0.9999514818191528, pos_tag=None, start_offset=1898, end_offset=1901),
                Entity(entity='st', label='PERSON', model_label='I-PER', description=None,
                       confidence=0.9999731779098511, pos_tag=None, start_offset=1901, end_offset=1903),
                Entity(entity='▁Million', label='ORG', model_label='I-ORG', description=None,
                       confidence=0.9999611377716064, pos_tag=None, start_offset=1934, end_offset=1941),
                Entity(entity='▁Victor', label='ORG', model_label='I-ORG', description=None,
                       confidence=0.999975323677063, pos_tag=None, start_offset=1942, end_offset=1948),
                Entity(entity='ies', label='ORG', model_label='I-ORG', description=None, confidence=0.9999688863754272,
                       pos_tag=None, start_offset=1948, end_offset=1951),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999123811721802, pos_tag=None, start_offset=2058, end_offset=2065),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999490976333618, pos_tag=None, start_offset=2066, end_offset=2070),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9997902512550354,
                       pos_tag=None, start_offset=2070, end_offset=2071),
                Entity(entity='▁Expedi', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9992576241493225, pos_tag=None, start_offset=2134, end_offset=2140),
                Entity(entity='tions', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9785085320472717, pos_tag=None, start_offset=2140, end_offset=2145),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9998486042022705, pos_tag=None, start_offset=2166, end_offset=2173),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999251365661621, pos_tag=None, start_offset=2174, end_offset=2178),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.999646782875061,
                       pos_tag=None, start_offset=2178, end_offset=2179),
                Entity(entity='▁Million', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999384880065918, pos_tag=None, start_offset=2256, end_offset=2263),
                Entity(entity='▁Lord', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999706745147705, pos_tag=None, start_offset=2264, end_offset=2268),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.9998822212219238,
                       pos_tag=None, start_offset=2268, end_offset=2269),
                Entity(entity='▁New', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999325275421143, pos_tag=None, start_offset=2270, end_offset=2273),
                Entity(entity='▁Horizon', label='MISC', model_label='I-MISC', description=None,
                       confidence=0.9999493360519409, pos_tag=None, start_offset=2274, end_offset=2281),
                Entity(entity='s', label='MISC', model_label='I-MISC', description=None, confidence=0.999575674533844,
                       pos_tag=None, start_offset=2281, end_offset=2282)]

    for entity in entities:
        single_model_aggregator.add(Entity.parse_obj(entity))

    composed_named_entities, entity_aggregates = single_model_aggregator.aggregate()
    assert len(entity_aggregates) == 13
    assert entity_aggregates["new horizonsORG"].count == 2
    assert entity_aggregates["new horizonsORG"].entity == "New Horizons"
