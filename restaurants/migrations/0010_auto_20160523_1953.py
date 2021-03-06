# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-23 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_restaurant_dishes'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='devise',
            field=models.CharField(choices=[(b'AED', b'United Arab Emirates Dirham'), (b'AFN', b'Afghanistan Afghani'), (b'ALL', b'Albania Lek'), (b'AMD', b'Armenia Dram'), (b'ANG', b'Netherlands Antilles Guilder'), (b'AOA', b'Angola Kwanza'), (b'ARS', b'Argentina Peso'), (b'AUD', b'Australia Dollar'), (b'AWG', b'Aruba Guilder'), (b'AZN', b'Azerbaijan New Manat'), (b'BAM', b'Bosnia and Herzegovina Convertible Marka'), (b'BBD', b'Barbados Dollar'), (b'BDT', b'Bangladesh Taka'), (b'BGN', b'Bulgaria Lev'), (b'BHD', b'Bahrain Dinar'), (b'BIF', b'Burundi Franc'), (b'BMD', b'Bermuda Dollar'), (b'BND', b'Brunei Darussalam Dollar'), (b'BOB', b'Bolivia Boliviano'), (b'BRL', b'Brazil Real'), (b'BSD', b'Bahamas Dollar'), (b'BTN', b'Bhutan Ngultrum'), (b'BWP', b'Botswana Pula'), (b'BYR', b'Belarus Ruble'), (b'BZD', b'Belize Dollar'), (b'CAD', b'Canada Dollar'), (b'CDF', b'Congo/Kinshasa Franc'), (b'CHF', b'Switzerland Franc'), (b'CLP', b'Chile Peso'), (b'CNY', b'China Yuan Renminbi'), (b'COP', b'Colombia Peso'), (b'CRC', b'Costa Rica Colon'), (b'CUC', b'Cuba Convertible Peso'), (b'CUP', b'Cuba Peso'), (b'CVE', b'Cape Verde Escudo'), (b'CZK', b'Czech Republic Koruna'), (b'DJF', b'Djibouti Franc'), (b'DKK', b'Denmark Krone'), (b'DOP', b'Dominican Republic Peso'), (b'DZD', b'Algeria Dinar'), (b'EGP', b'Egypt Pound'), (b'ERN', b'Eritrea Nakfa'), (b'ETB', b'Ethiopia Birr'), (b'EUR', b'Euro Member Countries'), (b'FJD', b'Fiji Dollar'), (b'FKP', b'Falkland Islands (Malvinas) Pound'), (b'GBP', b'United Kingdom Pound'), (b'GEL', b'Georgia Lari'), (b'GGP', b'Guernsey Pound'), (b'GHS', b'Ghana Cedi'), (b'GIP', b'Gibraltar Pound'), (b'GMD', b'Gambia Dalasi'), (b'GNF', b'Guinea Franc'), (b'GTQ', b'Guatemala Quetzal'), (b'GYD', b'Guyana Dollar'), (b'HKD', b'Hong Kong Dollar'), (b'HNL', b'Honduras Lempira'), (b'HRK', b'Croatia Kuna'), (b'HTG', b'Haiti Gourde'), (b'HUF', b'Hungary Forint'), (b'IDR', b'Indonesia Rupiah'), (b'ILS', b'Israel Shekel'), (b'IMP', b'Isle of Man Pound'), (b'INR', b'India Rupee'), (b'IQD', b'Iraq Dinar'), (b'IRR', b'Iran Rial'), (b'ISK', b'Iceland Krona'), (b'JEP', b'Jersey Pound'), (b'JMD', b'Jamaica Dollar'), (b'JOD', b'Jordan Dinar'), (b'JPY', b'Japan Yen'), (b'KES', b'Kenya Shilling'), (b'KGS', b'Kyrgyzstan Som'), (b'KHR', b'Cambodia Riel'), (b'KMF', b'Comoros Franc'), (b'KPW', b'Korea (North) Won'), (b'KRW', b'Korea (South) Won'), (b'KWD', b'Kuwait Dinar'), (b'KYD', b'Cayman Islands Dollar'), (b'KZT', b'Kazakhstan Tenge'), (b'LAK', b'Laos Kip'), (b'LBP', b'Lebanon Pound'), (b'LKR', b'Sri Lanka Rupee'), (b'LRD', b'Liberia Dollar'), (b'LSL', b'Lesotho Loti'), (b'LYD', b'Libya Dinar'), (b'MAD', b'Morocco Dirham'), (b'MDL', b'Moldova Leu'), (b'MGA', b'Madagascar Ariary'), (b'MKD', b'Macedonia Denar'), (b'MMK', b'Myanmar (Burma) Kyat'), (b'MNT', b'Mongolia Tughrik'), (b'MOP', b'Macau Pataca'), (b'MRO', b'Mauritania Ouguiya'), (b'MUR', b'Mauritius Rupee'), (b'MVR', b'Maldives (Maldive Islands) Rufiyaa'), (b'MWK', b'Malawi Kwacha'), (b'MXN', b'Mexico Peso'), (b'MYR', b'Malaysia Ringgit'), (b'MZN', b'Mozambique Metical'), (b'NAD', b'Namibia Dollar'), (b'NGN', b'Nigeria Naira'), (b'NIO', b'Nicaragua Cordoba'), (b'NOK', b'Norway Krone'), (b'NPR', b'Nepal Rupee'), (b'NZD', b'New Zealand Dollar'), (b'OMR', b'Oman Rial'), (b'PAB', b'Panama Balboa'), (b'PEN', b'Peru Sol'), (b'PGK', b'Papua New Guinea Kina'), (b'PHP', b'Philippines Peso'), (b'PKR', b'Pakistan Rupee'), (b'PLN', b'Poland Zloty'), (b'PYG', b'Paraguay Guarani'), (b'QAR', b'Qatar Riyal'), (b'RON', b'Romania New Leu'), (b'RSD', b'Serbia Dinar'), (b'RUB', b'Russia Ruble'), (b'RWF', b'Rwanda Franc'), (b'SAR', b'Saudi Arabia Riyal'), (b'SBD', b'Solomon Islands Dollar'), (b'SCR', b'Seychelles Rupee'), (b'SDG', b'Sudan Pound'), (b'SEK', b'Sweden Krona'), (b'SGD', b'Singapore Dollar'), (b'SHP', b'Saint Helena Pound'), (b'SLL', b'Sierra Leone Leone'), (b'SOS', b'Somalia Shilling'), (b'SPL*', b'Seborga Luigino'), (b'SRD', b'Suriname Dollar'), (b'STD', b'S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe Dobra'), (b'SVC', b'El Salvador Colon'), (b'SYP', b'Syria Pound'), (b'SZL', b'Swaziland Lilangeni'), (b'THB', b'Thailand Baht'), (b'TJS', b'Tajikistan Somoni'), (b'TMT', b'Turkmenistan Manat'), (b'TND', b'Tunisia Dinar'), (b'TOP', b"Tonga Pa'anga"), (b'TRY', b'Turkey Lira'), (b'TTD', b'Trinidad and Tobago Dollar'), (b'TVD', b'Tuvalu Dollar'), (b'TWD', b'Taiwan New Dollar'), (b'TZS', b'Tanzania Shilling'), (b'UAH', b'Ukraine Hryvnia'), (b'UGX', b'Uganda Shilling'), (b'USD', b'United States Dollar'), (b'UYU', b'Uruguay Peso'), (b'UZS', b'Uzbekistan Som'), (b'VEF', b'Venezuela Bolivar'), (b'VND', b'Viet Nam Dong'), (b'VUV', b'Vanuatu Vatu'), (b'WST', b'Samoa Tala'), (b'XAF', b'Communaut\xc3\xa9 Financi\xc3\xa8re Africaine (BEAC) CFA Franc BEAC'), (b'XCD', b'East Caribbean Dollar'), (b'XDR', b'International Monetary Fund (IMF) Special Drawing Rights'), (b'XOF', b'Communaut\xc3\xa9 Financi\xc3\xa8re Africaine (BCEAO) Franc'), (b'XPF', b'Comptoirs Fran\xc3\xa7ais du Pacifique (CFP) Franc'), (b'YER', b'Yemen Rial'), (b'ZAR', b'South Africa Rand'), (b'ZMW', b'Zambia Kwacha'), (b'ZWD', b'Zimbabwe Dollar')], default='EUR', max_length=10),
        ),
        migrations.AddField(
            model_name='dish',
            name='prix',
            field=models.FloatField(blank=True, null=True, verbose_name='prix'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='latitude'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='longitude'),
        ),
    ]
