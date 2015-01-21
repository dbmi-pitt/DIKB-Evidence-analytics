/**
 * Crayola colors in JSON format
 * from: https://gist.github.com/jjdelc/1868136
 */
var colors =

    [{"hex": "Amio-Aqueous-IV / Amiodarona             ", "label": "Amiodarone", "rgb": "(239, 222, 205)"},
    {"hex": "Apo-Triazo / Triazolam              ", "label": "Triazolam", "rgb": "(239, 222, 205)"},
    {"hex": "Acalix / Diltiazem              ", "label": "Diltiazem", "rgb": "(239, 222, 205)"},
    {"hex": "Cholestat / Simvastatina           ", "label": "Simvastatin", "rgb": "(239, 222, 205)"},
    {"hex": "Extina / Ketoconazol            ", "label": "Ketoconazole", "rgb": "(239, 222, 205)"},
    {"hex": "Anquil / Midazolam              ", "label": "Midazolam", "rgb": "(239, 222, 205)"},
    {"hex": "Artosin / 1-Butyl-3-tosylurea    ", "label": "Tolbutamide", "rgb": "(239, 222, 205)"},
    {"hex": "Dumirox / Fluvoxamina            ", "label": "Fluvoxamine", "rgb": "(239, 222, 205)"},
    {"hex": "Alplax / Alprazolam             ", "label": "Alprazolam", "rgb": "(239, 222, 205)"},
    {"hex": "Dutonin / Nefazodona             ", "label": "Nefazodone", "rgb": "(239, 222, 205)"},
    {"hex": "Diflucan / Fluconazole            ", "label": "Fluconazole", "rgb": "(239, 222, 205)"},
    {"hex": "Agopton / Lansoprazol            ", "label": "Lansoprazole", "rgb": "(239, 222, 205)"},
    {"hex": "Itrizole / Itraconazol            ", "label": "Itraconazole", "rgb": "(239, 222, 205)"},
    {"hex": "Altocor / 6-alpha-methylcompactin", "label": "Lovastatin", "rgb": "(239, 222, 205)"},
    {"hex": "Adofen / Fluoxetin              ", "label": "Fluoxetine", "rgb": "(239, 222, 205)"},
    {"hex": "Risperdal / Risperdone             ", "label": "Risperidone", "rgb": "(239, 222, 205)"},
    {"hex": "Effexor / Venlafaxine            ", "label": "Venlafaxine", "rgb": "(239, 222, 205)"},
    {"hex": "Atogal / Lipovastatinklonal     ", "label": "Atorvastatin", "rgb": "(239, 222, 205)"},
    {"hex": "Cipralex / Escitalopram-Oxalate   ", "label": "Escitalopram", "rgb": "(239, 222, 205)"},
    {"hex": "Cimetag / Cimetidin              ", "label": "Cimetidine", "rgb": "(239, 222, 205)"},
    {"hex": "Elixophyllin / 1,3-dimethyl           ", "label": "Theophylline", "rgb": "(239, 222, 205)"},
    {"hex": "Ariclaim / Duloxetine             ", "label": "Duloxetine", "rgb": "(239, 222, 205)"},
    {"hex": "Antra / OMEP                   ", "label": "Omeprazole", "rgb": "(239, 222, 205)"},
    {"hex": "Aloperidin / Haloperidol            ", "label": "Haloperidol", "rgb": "(239, 222, 205)"},
    {"hex": "Akne-Mycin / 3''-O-demethylery      ", "label": "Erythromycin", "rgb": "(239, 222, 205)"},
    {"hex": "Rythmol / Propafenona            ", "label": "Propafenone", "rgb": "(239, 222, 205)"},
    {"hex": "Ambien-CR / Zolpidemum             ", "label": "Zolpidem", "rgb": "(239, 222, 205)"},
    {"hex": "Cravit / L-ofloxacin            ", "label": "Levofloxacin", "rgb": "(239, 222, 205)"},
    {"hex": "Factive / Gemifloxacin-mesilate  ", "label": "Gemifloxacin", "rgb": "(239, 222, 205)"},
    {"hex": "Avelox / Moxifloxacin           ", "label": "Moxifloxacin", "rgb": "(239, 222, 205)"},
    {"hex": "Floxin / OFLX                   ", "label": "Ofloxacin", "rgb": "(239, 222, 205)"},
    {"hex": "Noxafil / Posaconazole           ", "label": "Posaconazole", "rgb": "(239, 222, 205)"},
    {"hex": "Vfend / VCZ                    ", "label": "Voriconazole", "rgb": "(239, 222, 205)"},
    {"hex": "Diflucan / Fluconazole            ", "label": "Fluconazole ", "rgb": "(239, 222, 205)"}];


$(function () {
  $('#nope').autocompleter({
        // marker for autocomplete matches
        highlightMatches: true,

        // object to local or url to remote search
        source: colors,

        // custom template
        template: '{{ label }} <span>({{ hex }})</span>',

        // show hint
        hint: true,

        // abort source if empty field
        empty: false,

        // max results
        limit: 5,

        callback: function (value, index, selected) {
            if (selected) {
                $('.icon').css('background-color', selected.hex);
            }
        }
    });
});
