alldatastruct = { 
    "page9": {
        "pagenum": 9,
        "tables": [
            {
                "tablename": "Indigenous student enrolments, 2006 to 2020",
                "tabledata":[
                    {
                        "chart_anchor_text": [
                            "Figure 1: Indigenous student enrolments, 2006 to 2020",
                            "Source: Department of Education, Skills and Employment 2022, Selected Higher Education Statistics – 2020 Student data,"
                        ],
                        "data": 
                            {
                                "left_right": ["8,816", "22,897"],
                                "top_bottom": ["-ignore","2020"],
                                "column_label": "indigenous_student_enrolment"
                            },
                        "other_columns": {
                            "year": {
                                "left_right": ["2006", "2020"],
                                "top_bottom": ["8,816","-ignore"],
                            }        
                        }
                    }
                ],
                "insights": 
"""
Indegenous student enrollments,
have almost trippled from the numbers in 2006.
""",
                "charttype": [
                    {
                        "charttype": "line",
                        "x_col": "year",
                        "y_series": [
                            {
                                "col": "indigenous_student_enrolment",
                                "label": "Indigenous Student Enrolments"
                            }
                        ],
                        
                    }
                ],
                "percent": False
            },
            {
                "tablename": "Share of Indigenous student enrolments, 2006 to 2020",
                "tabledata":[
                    {
                        "chart_anchor_text": [
                            "Figure 2: Share of Indigenous student enrolments, 2006 to 2020",
                            "Source: Department of Education, Skills and Employment 2022, Selected Higher Education Statistics – 2020 Student data,"
                        ],
                        "data": 
                            {
                                "left_right": ["1.22%", "2.04%"],
                                "top_bottom": ["-ignore","2020"],
                                "column_label": "share_indigenous_student_enrolment"
                            },
                        "other_columns": {
                            "year": {
                                "left_right": ["2006", "2020"],
                                "top_bottom": ["1.22%","-ignore"],
                            }        
                        }
                    }
                ],
                "insights": 
"""
The share has also grown 
but the share is still below 
the population share of 3.1%
""",
                "charttype": [
                    {
                        "charttype": "line",
                        "x_col": "year",
                        "y_series": [
                            {
                                "col": "share_indigenous_student_enrolment",
                                "label": "Share of Indigenous Student Enrolments"
                            }
                        ],
                        
                    }
                ],
                "percent": True
            }
        ]
    },
    "page13": {
        "pagenum": 13,
        "tables": [
            {
                "tablename": "Annual growth in undergraduate applications, 2013 to 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 5: Annual growth in undergraduate applications, 2013 to 2021",
                            "Source: Department of Education, Skills and Employment 2021, Undergraduate Applications Offers and Acceptances, unpublished data."
                        ],
                        "data": 
                            {
                                "left_right": ["6.7%", "2.4%"],
                                "top_bottom": ["Indigenous","2021"],
                                "column_label": "share_indigenous_student_enrolment"
                            },
                        "other_columns": {
                            "year": {
                                "left_right": ["2013", "2021"],
                                "top_bottom": ["-4.9%","-ignore"],
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            }  
                        }
                    }
                ],
                "insights": 
"""
In most years, Indigenous application 
is out growing non-indigenous.  
Observed negative growth in 2018 and 2021.
""",
                "charttype": [
                    {
                        "charttype": "line",
                        "x_col": "year",
                        "y_series": [
                            {
                                "col": "share_indigenous_student_enrolment",
                                "label": "Share of Indigenous Student Enrolments",
                                "filter": [("ind_no-ind","Indigenous")]
                            },
                            {
                                "col": "share_indigenous_student_enrolment",
                                "label": "Share of Non-Indigenous Student Enrolments",
                                "filter": [("ind_no-ind","Non-Indigenous")]
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page14": {
        "pagenum": 14,
        "tables": [
            {
                "tablename": "Share of undergraduate applications, by age, 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 6: Share of undergraduate applications, by age, 2021",
                            "Source: See Figure 5."
                        ],
                        "data": 
                            {
                                "left_right": ["56%", "6%"],
                                "top_bottom": ["15","Non-Indigenous"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "age_group": {
                                "vals": ['15 to 19', '20 to 24', '25 to 39', '40 to 64'], # it is easier just to define it like this as the spaces will chunk 15 to 19 into 3 blocks
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous"],
                                "chunk_size": 1
                            }  
                        }
                    },
                    {
                        "chart_anchor_text": [
                            "Figure 6: Share of undergraduate applications, by age, 2021",
                            "Source: See Figure 5."
                        ],
                        "data": 
                            {
                                "left_right": ["41%", "10%"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "age_group": {
                                "vals": ['15 to 19', '20 to 24', '25 to 39', '40 to 64'], # it is easier just to define it like this as the spaces will chunk 15 to 19 into 3 blocks
                            },
                            "ind_no-ind" : {
                                "vals": ["Non-Indigenous"],
                                "chunk_size": 1
                            }  
                        }
                    }                    
                ],
                "insights": 
"""
Indigenous students tend to enter Univerity ealier,
however there is a noticeable drop off at higher 
age brackets.
""",
                "charttype": None,
                
                # ok changed my mind not goin to write code for pie chart
                # [
                #     {
                #         "charttype": "line",
                #         "title": "Share of Indigenous applications by age",
                #         "labels": "age_group",
                #         "sizes": [
                #             {
                #                 "col": "values",
                #                 "filter": [("ind_no-ind", "Indigenous applications")]
                #             }
                #         ],
                #     },
                #     {
                #         "charttype": "line",
                #         "title": "Share of Indigenous population by age",
                #         "labels": "age_group",
                #         "sizes": [
                #             {
                #                 "col": "values",
                #                 "filter": [("ind_no-ind", "Indigenous population")]
                #             }
                #         ],
                #     }
                # ],
                "percent": True
            },
            {
                "tablename": "Share of Indigenous undergraduate applications compared to share of Indigenous population, by age, 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 7: Share of Indigenous undergraduate applications compared to share of Indigenous",
                            "15 to 19 20 to 24 25 to 39 40 to 64"
                        ],
                        "data": 
                            {
                                "left_right": ["1.6%", "2.4%"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "age_group": {
                                "vals": ['15 to 19', '20 to 24', '25 to 39', '40 to 64'], # it is easier just to define it like this as the spaces will chunk 15 to 19 into 3 blocks
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous applications","Indigenous population"],
                                "chunk_size": 1
                            }  
                        }
                    }
                ],
                "insights": 
"""
At the younger age group 15 to 24, 
the share of undergraduate appication 
is well below population parity.  
However at the older age group it is at 
or higher than the population share.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for Indigenous applications vs population (below 0 under-represented)",
                        "x_col": "age_group",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [("ind_no-ind","Indigenous applications")]
                            },
                            {
                                "col": "values",
                                "filter": [("ind_no-ind","Indigenous population")]
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page17": {
        "pagenum": 17,
        "tables": [
            {
                "tablename": "Nine-year completion rates of commencing Indigenous and non-Indigenous Bachelor degree students",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 11: Nine-year completion rates of commencing Indigenous and non-Indigenous Bachelor",
                            "Source: Department of Education, Skills and Employment 2022, Completion Rates of Higher Education Students – Cohort Analysis, 2005–2020."
                        ],
                        "data": 
                            {
                                "left_right": ["46.5%", "72.2%"],
                                "top_bottom": ["Indigenous","2005"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "year": {
                                "left_right": ["2005", "2012"],
                                "top_bottom": ["46.5%","-ignore"],
                                "remove": ["Cohort"],
                                "chunk_size": 2            
                            },            
                            "ind_no-ind" : {
                                "vals": ["Indigenous students","Non-Indigenous students"],
                                "chunk_size": 1
                            }  
                        }
                    }
                ],
                "insights": 
"""
Although the completion rates have improved 
for Indigenous students, it is still well 
below the non-indigenous population.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for Bachelor degree students, Indigenous vs Non-Indigenous (below 0 under-represented)",
                        "x_col": "year",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [("ind_no-ind","Indigenous students")]
                            },
                            {
                                "col": "values",
                                "filter": [("ind_no-ind","Non-Indigenous students")]
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page18": {
        "pagenum": 18,
        "tables": [
            {
                "tablename": "Share of Indigenous students commencing a Bachelor degree that never return – after four years",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 12: Share of Indigenous students commencing a Bachelor degree that never return – after",
                            "Source: See Figure 11."
                        ],
                        "data": 
                            {
                                "left_right": ["25.8%", "20.4%"],
                                "top_bottom": ["four","2005"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "year": {
                                "left_right": ["2005", "2017"],
                                "top_bottom": ["18.4%","cohort"],
                            },            
                        }
                    }
                ],
                "insights": 
"""
The rate of in-completions have been 
improving over the years, 
however there is an uptick in 2017.
""",
                "charttype": [
                    {
                        "charttype": "line",
                        "title": "Share of Indigenous students commencing a Bachelor degree students over time",
                        "x_col": "year",
                        "y_series": [
                            {
                                "col": "values",
                                "label": "Indigenous students"
                            }                        
                        ],
                    }
                ],
                "percent": True
            }
        ]        
    },
    "page19": {
        "pagenum": 19,
        "tables": [
            {
                "tablename": "Retention and success rates of domestic Bachelor degree students, Indigenous vs non-Indigenous, per cent",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "non-Indigenous, per cent",
                            "Source: Department of Education, Skills and Employment 2022, Visual Analytics–Attrition, retention and success rates."
                        ],
                        "data": 
                            {
                                "left_right": ["68.8%", "86.1%"],
                                "top_bottom": ["Indigenous","2008"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "year": {
                                "vals": ["2008","2018","2019",2020],
                                "chunk_size": 2            
                            },            
                            "rate_type":{
                                "vals": ["Success rates"],
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous students","Non-Indigenous students"],
                                "chunk_size": 1
                            }  
                        }
                    },
                    {
                        "chart_anchor_text": [
                            "non-Indigenous, per cent",
                            "Source: Department of Education, Skills and Employment 2022, Visual Analytics–Attrition, retention and success rates."
                        ],
                        "data": 
                            {
                                "left_right": ["74.0%", "86.8%"],
                                "top_bottom": ["Indigenous","2008"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "year": {
                                "vals": ["2008","2017","2018",2019],
                                "chunk_size": 2            
                            },            
                            "rate_type":{
                                "vals": ["Retention rates"],
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous students","Non-Indigenous students"],
                                "chunk_size": 1
                            }  
                        }
                    },
                    
                ],
                "insights": 
"""
The success and retention rates have remained stable 
for the past decade.  The indigenous rates are roughly 
10% lower than the non-indigenous groups.
Perhaps there is a mislabelling of the years, 
with inconsistent year labels between success and retention.
""",
                "charttype": [
                    {
                        "charttype": "line",
                        "title": "Success rates of domestic Bachelor degree students",
                        "x_col": "year",
                        "y_series": [
                            {
                                "col": "values",
                                "label": "Indigenous Students",
                                "filter": [
                                    ("rate_type","Success rates"),
                                    ("ind_no-ind","Indigenous students")
                                ]
                            },
                            {
                                "col": "values",
                                "label": "Non-Indigenous Students",
                                "filter": [
                                    ("rate_type","Success rates"),
                                    ("ind_no-ind","Non-Indigenous students")
                                ]
                            }
                        ],
                    },
                    {
                        "charttype": "line",
                        "title": "Retention rates of domestic Bachelor degree students",
                        "x_col": "year",
                        "y_series": [
                            {
                                "col": "values",
                                "label": "Indigenous Students",
                                "filter": [
                                    ("rate_type","Retention rates"),
                                    ("ind_no-ind","Indigenous students")
                                ]
                            },
                            {
                                "col": "values",
                                "label": "Non-Indigenous Students",
                                "filter": [
                                    ("rate_type","Retention rates"),
                                    ("ind_no-ind","Non-Indigenous students")
                                ]
                                    
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page20": {
        "pagenum": 20,
        "tables": [
            {
                "tablename": "Short-term graduate employment outcomes, 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 14: Short-term graduate employment outcomes, 2021",
                            "Source: Social Research Centre 2021, 2021 Graduate Outcomes Survey."
                        ],
                        "data": 
                            {
                                "left_right": ["76.8%", "90.8%"],
                                "top_bottom": ["Undergraduate","Full-time"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "course_type": {
                                "vals": ["Undergraduate", "Postgraduate coursework"],
                                "chunk_size": 4
                            },
                            "course_time": {
                                "vals": ["Full-time", "Overall"],
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous students", "Non-Indigenous students"],
                                "chunk_size": 1
                            },
                            "year": {
                                "vals": ["2021"],
                                "chunk_size": 1
                            }
                        }
                    }
                ],
                "insights": 
"""
A high percentage of Indigenous graduates 
are able to get employment, 4 months after completion, 
generally higher percentage compared to non-indigenous group.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for short term employment outcomes 2021, Undergraduate category (below 0 under-represented)",
                        "x_col": "course_time",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Undergraduate"),
                                    ("ind_no-ind","Indigenous students")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Undergraduate"),
                                    ("ind_no-ind","Non-Indigenous students")
                                ]
                            }
                        ],
                    },
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for short term employment outcomes 2021, Postgraduate coursework category (below 0 under-represented)",
                        "x_col": "course_time",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Postgraduate coursework"),
                                    ("ind_no-ind","Indigenous students")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Postgraduate coursework"),
                                    ("ind_no-ind","Non-Indigenous students")
                                ]
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page21": {
        "pagenum": 21,
        "tables": [
            {
                "tablename": "Short and medium-term full-time employment outcomes, for 2018 graduates",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 15: Short and medium-term full-time employment outcomes, for 2018 graduates",
                            "Source: Social Research Centre 2021, 2021 Graduate Outcomes Survey–Longitudinal."
                        ],
                        "data": 
                            {
                                "left_right": ["77.0%", "93.2%"],
                                "top_bottom": ["Undergraduate","Full-time"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "course_type": {
                                "vals": ["Undergraduate", "Postgraduate coursework"],
                                "chunk_size": 4
                            },
                            "course_time": {
                                "vals": ["Full-time", "Overall"],
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous students", "Non-Indigenous students"],
                                "chunk_size": 1
                            },
                            "year": {
                                "vals": ["2018"],
                                "chunk_size": 1
                            }
                        }
                    }
                ],
                "insights": 
"""
This is the 2018 chart and compared to the numbers 
from 2021, the indigenous employment opportunities 
have significantly improved.  Howerver the overall 
employment percentage has dropped in 2021.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for short term employment outcomes 2018, Undergraduate category (below 0 under-represented)",
                        "x_col": "course_time",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Undergraduate"),
                                    ("ind_no-ind","Indigenous students")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Undergraduate"),
                                    ("ind_no-ind","Non-Indigenous students")
                                ]
                            }
                        ],
                    },
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for short term employment outcomes 2018, Postgraduate coursework category (below 0 under-represented)",
                        "x_col": "course_time",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Postgraduate coursework"),
                                    ("ind_no-ind","Indigenous students")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("course_type","Postgraduate coursework"),
                                    ("ind_no-ind","Non-Indigenous students")
                                ]
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page25": {
        "pagenum": 25,
        "tables": [
            {
                "tablename": "Share of female staff by duties classification, 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 19: Share of female staff by duties classification, 2021",
                            "Source: Department of Education, Skills and Employment 2022, Unpublished HEIMS data."
                        ],
                        "data": 
                            {
                                "left_right": ["64.3%", "66.4%"],
                                "top_bottom": ["Indigenous","Level"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Level A", "Level B", "Level C", "Level D and above", "All academic staff", "Non-academic"], #still can't handle axis labels with spaces
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous staff", "Non-Indigenous staff"],
                                "chunk_size": 1
                            },
                            "year": {
                                "vals": ["2021"],
                                "chunk_size": 1
                            },
                            "gender": {
                                "vals": ["female"],
                                "chunk_size": 1
                            }
                        }
                    }
                ],
                "insights": 
"""
Accross all classificatins, Indigenous group 
have higher percentage of being female as compared 
to non-Indigenous groups.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for share of female staff by duties classifications 2021 (below 0 under-represented)",
                        "x_col": "duty_classification",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Indigenous staff")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Non-Indigenous staff")
                                ]
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page26": {
        "pagenum": 26,
        "tables": [
            {
                "tablename": "Proportion of staff aged under 40 by duties classification, 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 20: Proportion of staff aged under 40 by duties classification, 2021",
                            "Source: Department of Education, Skills and Employment 2022, Unpublished HEIMS data."
                        ],
                        "data": 
                            {
                                "left_right": ["53.5%", "40.5%"],
                                "top_bottom": ["Indigenous","Level"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Level A", "Level B", "Level C", "Level D and above", "All academic staff", "Non-academic"], #still can't handle axis labels with spaces
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous staff", "Non-Indigenous staff"],
                                "chunk_size": 1
                            },
                            "year": {
                                "vals": ["2021"],
                                "chunk_size": 1
                            },
                            "age_group": {
                                "vals": ["Under 40"],
                                "chunk_size": 1
                            }
                        }
                    }
                ],
                "insights": 
"""
Indigenous staff tends to be older than 
non-indigenous couterparts, 
especially in the academic setting.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for proportion of staff age under 40 by duties classifications 2021 (below 0 under-represented)",
                        "x_col": "duty_classification",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Indigenous staff")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Non-Indigenous staff")
                                ]
                            }
                        ],
                    }
                ],
                "percent": True
            }
        ]
    },
    "page27": {
        "pagenum": 27,
        "tables": [
            {
                "tablename": "Share of staff by academic duties classification, 2005, 2010 and 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 21: Share of staff by academic duties classification, 2005, 2010 and 2021",
                            "Source: Department of Education, Skills and Employment, Unpublished HEIMS data, various years."
                        ],
                        "data": 
                            {
                                "left_right": ["12.1%", "29.7%"],
                                "top_bottom": ["Level","17.0%"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Level D and above"], #still can't handle axis labels with spaces
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            },
                            "year": {
                                "left_right": ["2005", "2021"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "chunk_size": 2            
                            }, 
                        }
                    },
                    {
                        "chart_anchor_text": [
                            "Figure 21: Share of staff by academic duties classification, 2005, 2010 and 2021",
                            "Source: Department of Education, Skills and Employment, Unpublished HEIMS data, various years."
                        ],
                        "data": 
                            {
                                "left_right": ["17.0%", "29.7%"],
                                "top_bottom": ["29.7%","43.3%"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Level C"], #still can't handle axis labels with spaces
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            },
                            "year": {
                                "left_right": ["2005", "2021"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "chunk_size": 2            
                            }, 
                        }
                    },
                    {
                        "chart_anchor_text": [
                            "Figure 21: Share of staff by academic duties classification, 2005, 2010 and 2021",
                            "Source: Department of Education, Skills and Employment, Unpublished HEIMS data, various years."
                        ],
                        "data": 
                            {
                                "left_right": ["43.3%", "30.1%"],
                                "top_bottom": ["22.6%","27.7%"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Level B"], #still can't handle axis labels with spaces
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            },
                            "year": {
                                "left_right": ["2005", "2021"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "chunk_size": 2            
                            }, 
                        }
                    },
                    {
                        "chart_anchor_text": [
                            "Figure 21: Share of staff by academic duties classification, 2005, 2010 and 2021",
                            "Source: Department of Education, Skills and Employment, Unpublished HEIMS data, various years."
                        ],
                        "data": 
                            {
                                "left_right": ["27.7%", "17.5%"],
                                "top_bottom": ["30.1%","Indigenous"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Level A"], #still can't handle axis labels with spaces
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            },
                            "year": {
                                "left_right": ["2005", "2021"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "chunk_size": 2            
                            }, 
                        }
                    }
                ],
                "insights": 
"""
At level A and level B, the proportion 
of Indigenous staff is higher than the
non-indigenous staff.\n  At more senior levels, 
the indigenous staff numbers still lags behind 
the non-indigenous staff.  However the good sign 
is that, at senior levels, the numbers are growing 
year on year
""",
                "charttype": None,
                "percent": True
            }
        ]
    },
    "page28": {
        "pagenum": 28,
        "tables": [
            {
                "tablename": "Share of staff by academic functions, 2005, 2010 and 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 22: Share of staff by academic functions, 2005, 2010 and 2021",
                            "Source: Department of Education, Skills and Employment, Unpublished HEIMS data, various years."
                        ],
                        "data": 
                            {
                                "left_right": ["5.6%", "11.3%"],
                                "top_bottom": ["Teaching","13.9%"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Teaching and research"], #still can't handle axis labels with spaces
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            },
                            "year": {
                                "left_right": ["2005", "2021"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "chunk_size": 2            
                            }, 
                        }
                    },
                    {
                        "chart_anchor_text": [
                            "Figure 22: Share of staff by academic functions, 2005, 2010 and 2021",
                            "Source: Department of Education, Skills and Employment, Unpublished HEIMS data, various years."
                        ],
                        "data": 
                            {
                                "left_right": ["13.9%", "35.3%"],
                                "top_bottom": ["16.5%","80.6%"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Research only"], #still can't handle axis labels with spaces
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            },
                            "year": {
                                "left_right": ["2005", "2021"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "chunk_size": 2            
                            }, 
                        }
                    },
                    {
                        "chart_anchor_text": [
                            "Figure 22: Share of staff by academic functions, 2005, 2010 and 2021",
                            "Source: Department of Education, Skills and Employment, Unpublished HEIMS data, various years."
                        ],
                        "data": 
                            {
                                "left_right": ["80.6%", "53.4%"],
                                "top_bottom": ["29.8%","Indigenous"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Teaching only"], #still can't handle axis labels with spaces
                                "chunk_size": 1
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous", "Non-Indigenous"],
                                "chunk_size": 1
                            },
                            "year": {
                                "left_right": ["2005", "2021"],
                                "top_bottom": ["Indigenous","-ignore"],
                                "chunk_size": 2            
                            }, 
                        }
                    },
                ],
                "insights": 
"""
Teaching and Research roles have become 
more seperated over the years.  In more 
recent years, Indigenous staff are more 
likely to be teaching only and Indigenous 
staff proportions in `Research only`, 
still lags behind non-indegenous staff.
""",
                "charttype": None,
                "percent": True
            }
        ]
    },
    "page29": {
        "pagenum": 29,
        "tables": [
            {
                "tablename": "Indigenous staff, actual vs population parity figures, 2021",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 23: Indigenous staff, actual vs population parity figures, 2021",
                            "Source: UA estimates based on 2021 actual Indigenous staff numbers compared to if Indigenous staff numbers are at 3.1 per cent"
                        ],
                        "data": 
                            {
                                "left_right": ["99", "2068"],
                                "top_bottom": ["-ignore","Teaching-only"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "duty_classification": {
                                "vals": ["Teaching-only", "Research-only", "Teaching and research", "Other function"], #still can't handle axis labels with spaces
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Indigenous staff (actual numbers)", "Population parity figure"],
                                "chunk_size": 1
                            }
                        }
                    }
                ],
                "insights":
"""
In terms of types of roles, the sector would have
needed to employ an extra 90 Indigenous staff in
teaching-only roles, 411 in research-only roles and
570 in roles that combined teaching and research
in 2021.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for proportion of actual vs population parity 2021 (below 0 under-represented)",
                        "x_col": "duty_classification",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Indigenous staff (actual numbers)")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Population parity figure")
                                ]
                            }
                        ],
                    }
                ],
                "percent": False
            }
        ]
    },
    "page32": {
        "pagenum": 32,
        "tables": [
            {
                "tablename": "Indigenous postgraduate student, actual and population parity figures, 2020",
                "tabledata": [
                    {
                        "chart_anchor_text": [
                            "Figure 27: Indigenous postgraduate student, actual and population parity figures, 2020",
                            "Source: UA estimates based on 2020 actual Indigenous enrolments and award course completions compared to if Indigenous enrolments and"
                        ],
                        "data": 
                            {
                                "left_right": ["743", "2009"],
                                "top_bottom": ["Actual","Postgraduate"],
                                "column_label": "values"
                            },
                        "other_columns": {
                            "course_type": {
                                "vals": ["Postgraduate research", "Postgraduate coursework"], #still can't handle axis labels with spaces
                                "chunk_size": 2
                            },
                            "ind_no-ind" : {
                                "vals": ["Actual Indigenous students", "Population parity figure"],
                                "chunk_size": 1
                            },
                            "course_status": {
                                "vals": ["Enrolment", "Award completions"], #still can't handle axis labels with spaces
                                "chunk_size": 4
                            },
                        }
                    }
                ],
                "insights": 
"""
Througout this report, we have seen that the 
Indigenous representation in acamedic settings 
has improved greatly in the past decade.  
However this final chart show that much more work 
is needed to be done if we want to reach population 
parity of 3.1%.
""",
                "charttype": [
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for postgraduate student, actual vs population parity for Enrolment 2021 (below 0 under-represented)",
                        "x_col": "course_type",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Actual Indigenous students"),
                                    ("course_status","Enrolment")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Population parity figure"),
                                    ("course_status","Enrolment")
                                ]
                            }
                        ],
                    },
                    {
                        "charttype": "gap",
                        "title": "Gap/Delta chart for postgraduate student, actual vs population parity for Award completion 2021 (below 0 under-represented)",
                        "x_col": "course_type",
                        "y_series": [
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Actual Indigenous students"),
                                    ("course_status","Award completions")
                                ]
                            },
                            {
                                "col": "values",
                                "filter": [
                                    ("ind_no-ind","Population parity figure"),
                                    ("course_status","Award completions")
                                ]
                            }
                        ],
                    }
                ],
                "percent": False
            }
        ]
    }
    
}
