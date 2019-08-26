from django.test import TestCase
from django.urls import reverse

from .models import Mineral
from .utils import get_mineral_groups

class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="test",
        )
        self.assertEqual(mineral.name, "test")

class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Valentinite",
            image_filename="Valentinite.jpg",
            image_caption="A sample of valentinite from Algeria (size: 6.9 x 4.4 x 3.3 cm)",
            category="Oxide",
            formula="Sb<sub>2</sub>O<sub>3</sub>",
            strunz_classification="04.CB.55",
            crystal_system="Orthorhombic",
            unit_cell="a = 4.91 \u00c5, b = 12.46 \u00c5, c = 5.42 \u00c5; Z = 4",
            color="Colorless, snow-white, pale yellow, pink, gray to brownish",
            crystal_symmetry="Orthorhombic (2/m 2/m 2/m) dipyramidal",
            cleavage="{110}, perfect; {010}, imperfect",
            mohs_scale_hardness="2.5\u20133",
            luster="Adamantine, pearly on cleavages",
            streak="White",
            diaphaneity="Transparent to translucent",
            optical_properties="Biaxial (-)",
            refractive_index="n\u03b1 = 2.180 n\u03b2 = 2.350 n\u03b3 = 2.350",
            crystal_habit="Prismatic crystals, sometimes flattened, fan-shaped or stellate aggregates of crystals; lamellar, columnar, granular, massive.",
            specific_gravity="5.76",
            group="Oxides"
        )

        self.mineral2 = Mineral.objects.create(
            name="test",
            image_filename="test",
            image_caption="test",
            category="test",
            formula="test",
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'id': self.mineral.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_mineral_filter_by_first_letter(self):
        resp = self.client.get(reverse('minerals:list'), {'letter': 'A'})
        self.assertEqual(resp.status_code, 200)
        minerals = resp.context['minerals']
        for mineral in minerals:
            self.assertEqual(mineral.name[0], 'A')

    def test_mineral_filter_by_group(self):
        resp = self.client.get(reverse('minerals:list'), {'group': 'Silicates'})
        self.assertEqual(resp.status_code, 200)
        minerals = resp.context['minerals']
        for mineral in minerals:
            self.assertEqual(mineral.group, 'Silicates')

        resp = self.client.get(reverse('minerals:list'), {'group': 'Other'})
        self.assertEqual(resp.status_code, 200)
        minerals = resp.context['minerals']
        for mineral in minerals:
            self.assertNotIn(mineral.group, get_mineral_groups())

    def test_mineral_text_search(self):
        resp = self.client.get(reverse('minerals:list'), {'q': 'ap'})
        self.assertEqual(resp.status_code, 200)
        minerals = resp.context['minerals']
        for mineral in minerals:
            self.assertIn('ap', mineral.name.lower())
