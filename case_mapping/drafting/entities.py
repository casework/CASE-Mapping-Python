from ..base import FacetEntity, ObjectEntity, unpack_args_array


class FacetPassiveDNS(FacetEntity):
    def __init__(
        self, time_first=None, time_last=None, record_type=None, domain=None, ip=None
    ):
        """
        The characteristics of a block of information returned by PassiveDNS gadget.
        :param ip: The IPv4 address (may be none if the IP address is the source input)
        :param domain: The domain (may be none if the domain is the source input)
        :param time_first: An ISO8601 timestamp, indicating the first time the domain was observed
        :param time_last: An ISO8601 timestamp, indicating the last time the domain was observed
        :param record_type: The DNS record type (like 'A', 'AAA', etc.)
        """
        super().__init__()
        if ip:
            self["@type"] = "drafting:PassiveDnsIPFacet"

            self._str_vars(
                **{
                    "drafting:pdnsRecordType": record_type,
                    "drafting:pdnsIP": ip,
                }
            )
            self._datetime_vars(
                **{
                    "drafting:pdnsFirstSeen": time_first,
                    "drafting:pdnsLastSeen": time_last,
                }
            )
        else:
            self["@type"] = "drafting:PassiveDnsDomainFacet"

            self._str_vars(
                **{
                    "drafting:pdnsRecordType": record_type,
                    "drafting:pdnsDomain": domain,
                }
            )
            self._datetime_vars(
                **{
                    "drafting:pdnsFirstSeen": time_first,
                    "drafting:pdnsLastSeen": time_last,
                }
            )


class FacetTornodeInfo(FacetEntity):
    def __init__(
        self,
        router_name=None,
        country_code=None,
        orport=None,
        dirport=None,
        platform=None,
        ip=None,
        domain=None,
    ):
        """
        The characteristics of a block of information returned by TornodeDetector gadget.
        :param router_name: A tornode router name
        :param country_code: The country code of origin (like IE, or DE)
        :param orport: The onion router port (like 9001)
        :param dirport: The onion directory port (like 9030)
        :param ip: An IPv4 Address
        :param domain: The tor hostname
        """
        super().__init__()

        # The facet type and content depend on the input (ip OR hostame/domain)
        if ip:
            self["@type"] = "drafting:TornodeInfoIPFacet"

            self._str_vars(
                **{
                    "drafting:tornodeRouterName": router_name,
                    "drafting:tornodeCountryCode": country_code,
                    "drafting:tornodeORPort": orport,
                    "drafting:tornodeDirPort": dirport,
                    "drafting:tornodePlatform": platform,
                    "drafting:tornodeDomain": domain,
                }
            )

        else:
            self["@type"] = "drafting:TornodeInfoDomainFacet"

            self._str_vars(
                **{
                    "drafting:tornodeRouterName": router_name,
                    "drafting:tornodeCountryCode": country_code,
                    "drafting:tornodeORPort": orport,
                    "drafting:tornodeDirPort": dirport,
                    "drafting:tornodePlatform": platform,
                    "drafting:tornodeIP": ip,
                }
            )


class FacetLocalInternetRegistry(FacetEntity):
    def __init__(self, isp_name=None):
        """
        Used to define an ISP name
        :param isp_name: The ISP (like HEAnet)
        """
        super().__init__()
        self["@type"] = "drafting:LocalInternetRegistryFacet"
        self._str_vars(**{"drafting:ispName": isp_name})


class ObservablePort(ObjectEntity):
    def __init__(self, port, has_changed=None, state=None):
        """
        Used to represent a network port
        :param has_changed:
        :param state:
        :param hostname: The value for this object - a port (integer like 80 or 443)
        """
        super().__init__()
        self["@type"] = "drafting:NetworkPort"
        self._str_vars(**{"uco-observable:state": state})
        self._int_vars(**{"uco-observable:port": port})
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})


# it seems redundant, the identity:Organization class can be used instead
# class FacetOrganization(FacetEntity):
#    def __init__(self, org=None):
#        """
#        Used to define the organisation that an ISP assigns an IP address block to.
#        :param org: An organisation registered to an IP address block (like UCD Campus Network)
#        """
#        super().__init__()
#        self["@type"] = "drafting:OrganizationFacet"
#        self._str_vars(**{"drafting:organization": org})


class FacetBlockHasherScan(FacetEntity):
    def __init__(
        self,
        total_blocks=None,
        target=None,
        unknown=None,
        os=None,
        csam=None,
        malware=None,
        zeros=None,
        ones=None,
        validated_category=None,
        existing_or_invalid=None,
    ):
        super().__init__()
        self["@type"] = "drafting:BlockHasherScanFacet"
        self._str_vars(
            **{
                "drafting:bhsTotalBlocks": total_blocks,
                "drafting:bhsValidatedCategory": validated_category,
                "drafting:bhsExistingOrInvalid": existing_or_invalid,
                "drafting:bhsCategoryZeroBlocks": zeros,
                "drafting:bhsCategoryOneBlocks": ones,
                "drafting:bhsCategoryTemporaryTarget": target,
                "drafting:bhsCategoryUnknown": unknown,
                "drafting:bhsCategoryOS": os,
                "drafting:bhsCategoryCsam": csam,
                "drafting:bhsCategoryMalware": malware,
            }
        )


class FacetBlockHasherUpload(FacetEntity):
    def __init__(
        self, source_file=None, bhash=None, fhash=None, category=None, rejected="False"
    ):
        super().__init__()
        self["@type"] = "drafting:BlockHasherUploadFacet"
        self._str_vars(
            **{
                "drafting:bhuBlockHash": bhash,
                "drafting:bhuFileHash": fhash,
                "drafting:bhuCategory": category,
                "drafting:bhuRejected": rejected,
            }
        )


class FacetSocialMediaActivity(FacetEntity):
    def __init__(
        self,
        body=None,
        page_title=None,
        author_identifier=None,
        author_name=None,
        activity_type=None,
        reactions_count=None,
        shares_count=None,
        comments_count=None,
        account_identifier=None,
        created_time=None,
        application=None,
        url=None,
    ):
        """
        Used to represent activity on social platfomrs
        :param body: The text of the post/message
        :param page_title: The title of the page where the activity has been carried out
        :param author_identifier: the author identifier of the post published on the social media
        :param author_identifier: the author name of the post published on the social media
        :param reactions_count: the number of reactions to that post
        :param shares_count: the number of shares to that post
        :param activity_type: activity type of that post
        :param comment_count: he number of comments to that post
        :param account_identifier: the account identifier on which the post was published
        :param created_time: the date-time whene the post was published
        :param application: the application used for creating the post
        :param application: the URL of the post
        """
        super().__init__()

        self["@type"] = "drafting:SocialMediaActivityFacet"

        self._str_vars(
            **{
                "uco-observable:body": body,
                "uco-observable:pageTitle": page_title,
                "drafting:authorIdentifier": author_identifier,
                "drafting:authorName": author_name,
                "drafting:activityType": activity_type,
                "uco-observable:accountIdentifier": account_identifier,
            }
        )
        self._nonegative_int_vars(
            **{
                "drafting:reactionsCount": reactions_count,
                "drafting:sharesCount": shares_count,
                "drafting:commentsCount": comments_count,
            }
        )

        self._datetime_vars(
            **{
                "uco-observable:observableCreatedTime": created_time,
            }
        )

        self._node_reference_vars(
            **{
                "uco-observable:application": application,
                "uco-observable:url": url,
            }
        )


class FacetNIO(FacetEntity):
    def __init__(self, **kwargs):
        """
        Blank facet for stuff not in ontology???
        :param kwargs: Any additional user-specified (perhaps non-CASE) entries. (e.g., state="corrupted", notable=True)
        """
        super().__init__()
        self["@type"] = "drafting:dump"

        self["drafting:dumpResults"] = {
            "@type": "drafting:dumpResultsDictionary",
            "drafting:entry": list(),
        }
        for k, v in kwargs.items():
            if v and v not in ["", " "]:
                if isinstance(v, str):
                    item = {
                        "@type": "drafting:dumpResultsDictionaryEntry",
                        "drafting:key": k,
                        "drafting:stringValue": v,
                    }
                elif isinstance(v, dict):
                    item = {
                        "@type": "drafting:dumpResultsDictionaryEntry",
                        "drafting:key": k,
                        "drafting:dictionaryListValue": [v[k] for k in v],
                    }  # flatten {"0": xxx, "1": yyy} to [{xxx}, {yyy}]
                else:
                    item = {
                        "@type": "drafting:dumpResultsDictionaryEntry",
                        "drafting:key": k,
                        "drafting:stringValue": str(v),
                    }
                self["drafting:dumpResults"]["drafting:entry"].append(item)


class FacetMachineLearningResults(FacetEntity):
    def __init__(self, version=None, toolname=None, rendered_image_path=None, **kwargs):
        """
        Specifies a dictinary for accepting of items that may be output by numerous ML models or tools.
        :param kwargs: The user provided key/value pairs of machine learning items (e.g., BBOX=[215, 412, 118, 294], etc.).
        """
        super().__init__()
        self["@type"] = "drafting:machineLearningResultFacet"
        self._str_vars(
            **{
                "drafting:machineLearningModel": toolname,
                # todo: this should be some observable defining the model (or a tool:Tool?)
                "drafting:machineLearningModelVersion": version,
                "drafting:machineLearningRenderedImage": rendered_image_path,
            }
        )

        self["drafting:machineLearningResults"] = {
            "@type": "drafting:MLInferenceDictionary",
            "drafting:entry": list(),
        }
        for k, v in kwargs.items():
            if v and v not in ["", " "]:
                if isinstance(v, str):
                    item = {
                        "@type": "drafting:MLInferenceDictionaryEntry",
                        "drafting:key": k,
                        "drafting:stringValue": v,
                    }
                elif isinstance(v, list):
                    item = {
                        "@type": "drafting:MLInferenceDictionaryEntry",
                        "drafting:appendkey": k,
                        "drafting:listValue": str(v),
                    }
                elif isinstance(v, dict):
                    item = {
                        "@type": "drafting:MLInferenceDictionaryEntry",
                        "drafting:key": k,
                        "drafting:dictValue": str(v),
                    }
                else:
                    item = {
                        "@type": "drafting:MLInferenceDictionaryEntry",
                        "drafting:key": k,
                        "drafting:unknownTypeValue": str(v),
                    }
                self["drafting:machineLearningResults"]["drafting:entry"].append(item)


class FacetAnpr(FacetEntity):
    def __init__(self, anprPlate=None, anprTimestamp=None, anprLocation=None):
        """
        Characteristics of the ANPR Facet.
        :param anprPlate: Vehicle registartion as recorded by ANPR system
        :param anprTimestamp: Timestamp at which ANPR system recorded passing of registration
        :param anprLocation: Location of vehicle OR Location of recording i.e. "Berlin bridge 1"
        """
        super().__init__()
        self["@type"] = "drafting:anprLog"
        self._str_vars(
            **{
                "drafting:anpr_registrationPlate": anprPlate,
                # todo: registration plate should be conceptable in case/uco
                "drafting:anpr_timeStamp": anprTimestamp,
                # todo: Find source material to see what kind of timestamps are used
                "drafting:anpr_Location": anprLocation,
            }
        )  # todo: this is an overlap and should be added in a better way ? Also there should be more properties added to this however we do not have ANPR source materials available


# class FacetSearchedItem(FacetEntity):
#     def __init__(
#         self,
#         search_value=None,
#         search_result=None,
#         application=None,
#         search_launch_time=None,
#     ):
#         super().__init__()
#         self["@type"] = "drafting:SearchedItemFacet"
#         self._str_vars(
#             **{
#                 "drafting:searchValue": search_value,
#                 "drafting:searchResult": search_result,
#             }
#         )
#         self._datetime_vars(
#             **{"drafting:searchLaunchedTime": search_launch_time}
#         )
#         self._node_reference_vars(**{"uco-observable:application": application})


# bette to use EventRecordFacet

# class FacetLogEntries(FacetEntity):
#     def __init__(
#         self,
#         log_type=None,
#         reference=None,
#         paid_currency=None,
#         exchange_currency=None,
#         entry_category=None,
#         entry_datetime=None,
#         amount_paid=None,
#         exchange_amount=None,
#         exchange_rate=None,
#     ):
#         super().__init__()
#         self["@type"] = "drafting:LogEntriesFacet"
#         self._str_vars(
#             **{
#                 "drafting:logType": log_type,
#                 "drafting:logReference": reference,
#                 "drafting:logPaidCurrency": paid_currency,
#                 "drafting:logExchangeCurrency": exchange_currency,
#                 "drafting:logEntryCategory": entry_category,
#             }
#         )
#         self._datetime_vars(**{"drafting:logEntryTime": entry_datetime})
#         self._float_vars(
#             **{
#                 "drafting:logPaidAmount": amount_paid,
#                 "drafting:logExchangeAmount": exchange_amount,
#                 "drafting:logExchangeRate": exchange_rate,
#             }
#         )


class FacetCmsKeyValue(FacetEntity):
    def __init__(self, key=None, value=None):
        super().__init__()
        self["@type"] = "drafting:CmsKeyValueFacet"
        self._str_vars(**{"drafting:CmsKey": key, "drafting:CmsValue": value})


############################################
#  CLASSES BELOW USED BY NLP-ORCHESTRATOR  #
############################################


class FacetMachineLearningJob(FacetEntity):
    def __init__(self, inputs=None, model_name=None):
        super().__init__()
        self["@type"] = "drafting:MachineLearningJobFacet"
        self._str_vars(**{"drafting:modelName": model_name})
        self._node_reference_vars(**{"drafting:inputs": inputs})

    @unpack_args_array
    def append_inputs(self, *args):
        self._append_refs("drafting:inputs", *args)


class FacetNerEntity(FacetEntity):
    def __init__(
        self, entity_value=None, entity_type=None, occurrences=None, ml_job=None
    ):
        super().__init__()
        self["@type"] = "drafting:NerEntityFacet"
        self._str_vars(
            **{
                "drafting:entityValue": entity_value,
                "drafting:entityType": entity_type,
            }
        )
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})
        self["drafting:entityOccurrences"] = TextIntervals(indexed_items=occurrences)
        self["drafting:entityOccurrences"].pop("@id")
        self["drafting:entityOccurrences"].pop("@type")

    @unpack_args_array
    def append_messages(self, messages):
        self["uco-observable:message"].append_indexed_items(messages)


class FacetTextInterval(FacetEntity):
    def __init__(self, start_index, end_index, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:TextIntervalFacet"
        self._int_vars(
            **{
                "drafting:startIndex": start_index,
                "drafting:endIndex": end_index,
            }
        )
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class TextIntervals(ObjectEntity):
    def __init__(self, indexed_items=None):
        super().__init__()
        self["@type"] = "drafting:TextIntervals"
        self.append_indexed_items(indexed_items)


class FacetExtractedUrl(FacetEntity):
    def __init__(self, url=None, start_index=None, end_index=None, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:ExtractedUrlFacet"
        self._node_reference_vars(
            **{
                "uco-observable:url": url,
            }
        )
        self._int_vars(
            **{
                "drafting:startIndex": start_index,
                "drafting:endIndex": end_index,
            }
        )
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetExtractedTopic(FacetEntity):
    def __init__(self, topic=None, probability=None, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:ExtractedTopicFacet"
        self._str_vars(**{"drafting:topic": topic})
        self._float_vars(**{"drafting:probability": probability})
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetSentimentAnalysisResult(FacetEntity):
    def __init__(self, sentiment_value=None, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:SentimentAnalysisResultFacet"
        self._float_vars(**{"drafting:sentimentValue": sentiment_value})
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetTextSummarizationResult(FacetEntity):
    def __init__(self, summarized_text=None, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:TextSummarizationResultFacet"
        self._str_vars(**{"drafting:summarizedText": summarized_text})
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetTextAnnotationResult(FacetEntity):
    def __init__(self, annotated_text=None, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:TextAnnotationResultFacet"
        self._str_vars(**{"drafting:annotatedText": annotated_text})
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetTranslationResult(FacetEntity):
    def __init__(
        self,
        source_language=None,
        target_language=None,
        source_input=None,
        target_output=None,
        ml_job=None,
    ):
        super().__init__()
        self["@type"] = "drafting:TranslationResultFacet"
        self._str_vars(
            **{
                "drafting:sourceLanguage": source_language,
                "drafting:targetLanguage": target_language,
                "drafting:sourceInput": source_input,
                "drafting:targetText": target_output,
            }
        )
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetLanguageDetectionResult(FacetEntity):
    def __init__(self, source_language=None, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:LanguageDetectionResultFacet"
        self._str_vars(**{"drafting:sourceLanguage": source_language})
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetStylometryResults(FacetEntity):
    def __init__(
        self,
        pos_aux=None,
        pos_noun=None,
        pos_num=None,
        pos_other=None,
        pos_punct=None,
        pos_sym=None,
        pos_verb=None,
        wl_2=None,
        wl_3=None,
        wl_4=None,
        wl_5=None,
        wl_6=None,
        wl_7=None,
        wl_8=None,
        wl_9=None,
        wl_other=None,
        number_of_sentences=None,
        avg_sl=None,
        avg_wl=None,
        hx=None,
        ttr=None,
        ml_job=None,
        model_type=None,
    ):
        super().__init__()
        self["@type"] = "drafting:StylometryResultsFacet"
        self._str_vars(**{"drafting:modelType": model_type})
        self._int_vars(**{"drafting:numberOfSentences": number_of_sentences})
        self._float_vars(
            **{
                "drafting:avgSentenceLength": avg_sl,
                "drafting:avgWordLength": avg_wl,
                "drafting:hxVocabularyRichness": hx,
                "drafting:ttrVocabularyRichness": ttr,
                "drafting:partOfSpeechAux": pos_aux,
                "drafting:partOfSpeechNoun": pos_noun,
                "drafting:partOfSpeechNumber": pos_num,
                "drafting:partOfSpeechPunctuation": pos_punct,
                "drafting:partOfSpeechSymbol": pos_sym,
                "drafting:partOfSpeechVerv": pos_verb,
                "drafting:characterLength2": wl_2,
                "drafting:characterLength3": wl_3,
                "drafting:characterLength4": wl_4,
                "drafting:characterLength5": wl_5,
                "drafting:characterLength6": wl_6,
                "drafting:characterLength7": wl_7,
                "drafting:characterLength8": wl_8,
                "drafting:characterLength9": wl_9,
                "drafting:characterLengthOther": wl_other,
            }
        )
        self._node_reference_vars(**{"drafting:machineLearningJob": ml_job})


class FacetStylometrySimilarity(FacetEntity):
    def __init__(
        self,
        authors=None,
        ml_job=None,
        lexical=None,
        vocabulary=None,
        function_words=None,
        word_length_frequency=None,
        pos=None,
        embeddings=None,
        similarity=None,
    ):
        super().__init__()
        self["@type"] = "drafting:StylometrySimilarityFacet"
        self._float_vars(
            **{
                "drafting:lexicalFeaturesSimilarity": lexical,
                "drafting:vocabularySimilarity": vocabulary,
                "drafting:functionWordsSimilarity": function_words,
                "drafting:wordLengthFrequencySimilarity": word_length_frequency,
                "drafting:partOfSpeechSimilarity": pos,
                "drafting:embeddingsSimilarity": embeddings,
                "drafting:overallSimilarity": similarity,
            }
        )
        self._node_reference_vars(
            **{
                "drafting:authors": authors,
                "drafting:machineLearningJob": ml_job,
            }
        )

    @unpack_args_array
    def append_authors(self, *args):
        self._append_refs("drafting:authors", *args)


class FacetDocumentCollection(FacetEntity):
    def __init__(self, authors=None, documents=None, ml_job=None):
        super().__init__()
        self["@type"] = "drafting:DocumentCollectionFacet"
        self._node_reference_vars(
            **{
                "drafting:authors": authors,
                "drafting:documents": documents,
                "drafting:machineLearningJob": ml_job,
            }
        )


class FacetKddKeyInfo(FacetEntity):
    def __init__(
        self,
        key_name=None,
        times_occurred=None,
        contains_values=None,
        most_freq_val=None,
        most_freq_occurrence_prob=None,
        val_occurrence_prob_avg=None,
        val_occurrence_prob_stdev=None,
        most_freq_val_occurrences=None,
        avg_occurrences=None,
        stdev_occurrences=None,
        ml_job=None,
    ):
        super().__init__()
        self["@type"] = "drafting:KddKeyInfoFacet"
        self._int_vars(
            **{
                "drafting:timesOccurred": times_occurred,
                "drafting:mostFrequentValueOccurrences": most_freq_val_occurrences,
            }
        )
        self._str_vars(
            **{
                "drafting:mostFrequentValue": most_freq_val,
                "drafting:keyName": key_name,
            }
        )
        self._float_vars(
            **{
                "drafting:mostFrequentValueOccurrenceProb": most_freq_occurrence_prob,
                "drafting:averageOccurrenceProb": val_occurrence_prob_avg,
                "drafting:stDevOccurrenceProb": val_occurrence_prob_stdev,
                "drafting:averageOccurrences": avg_occurrences,
                "drafting:stDevOccurrences": stdev_occurrences,
            }
        )
        self._node_reference_vars(
            **{
                "drafting:containsValues": contains_values,
                "drafting:machineLearningJob": ml_job,
            }
        )

    @unpack_args_array
    def append_values(self, *args):
        self._append_refs("drafting:containsValues", *args)


class FacetKddValueInfo(FacetEntity):
    def __init__(
        self,
        value=None,
        times_occurred=None,
        occurrence_prob=None,
        support=None,
        ml_job=None,
    ):
        super().__init__()
        self["@type"] = "drafting:KddValueInfoFacet"
        self._int_vars(
            **{
                "drafting:timesOccurred": times_occurred,
            }
        )
        self._str_vars(
            **{
                "drafting:value": value,
            }
        )
        self._float_vars(
            **{
                "drafting:support": support,
                "drafting:occurrenceProb": occurrence_prob,
            }
        )
        self._node_reference_vars(
            **{
                "drafting:machineLearningJob": ml_job,
            }
        )


class FacetKddKeyCombination(FacetEntity):
    def __init__(
        self,
        support=None,
        times_occurred=None,
        key_1=None,
        key_2=None,
        key_3=None,
        value_1=None,
        value_2=None,
        value_3=None,
        ml_job=None,
    ):
        super().__init__()
        self["@type"] = "drafting:KddKeyCombinationFacet"
        self._int_vars(
            **{
                "drafting:timesOccurred": times_occurred,
            }
        )
        self._str_vars(
            **{
                "drafting:combinationKey1": key_1,
                "drafting:combinationKey2": key_2,
                "drafting:combinationKey3": key_3,
                "drafting:combinationValue1": value_1,
                "drafting:combinationValue2": value_2,
                "drafting:combinationValue3": value_3,
            }
        )
        self._float_vars(
            **{
                "drafting:support": support,
            }
        )
        self._node_reference_vars(
            **{
                "drafting:machineLearningJob": ml_job,
            }
        )


class FacetKddKeyRule(FacetEntity):
    def __init__(
        self,
        key_x=None,
        value_x=None,
        support_x=None,
        key_y=None,
        value_y=None,
        support_y=None,
        key_x_1of2=None,
        key_x_2of2=None,
        key_y_1of2=None,
        key_y_2of2=None,
        value_x_1of2=None,
        value_x_2of2=None,
        value_y_1of2=None,
        value_y_2of2=None,
        support=None,
        confidence=None,
        lift=None,
        cf=None,
        subconfidenceratio=None,
        ml_job=None,
    ):
        super().__init__()
        self["@type"] = "drafting:KddKeyRuleFacet"
        self._str_vars(
            **{
                "drafting:ruleKeyX": value_x,
                "drafting:ruleKeyX1of2": value_x_1of2,
                "drafting:ruleKeyX2of2": value_x_2of2,
                "drafting:ruleKeyY": value_y,
                "drafting:ruleKeyY1of2": value_y_1of2,
                "drafting:ruleKeyY2of2": value_y_2of2,
                "drafting:ruleValueX": value_x,
                "drafting:ruleValueX1of2": value_x_1of2,
                "drafting:ruleValueX2of2": value_x_2of2,
                "drafting:ruleValueY": value_y,
                "drafting:ruleValueY1of2": value_y_1of2,
                "drafting:ruleValueY2of2": value_y_2of2,
            }
        )
        self._float_vars(
            **{
                "drafting:support": support,
                "drafting:confidence": confidence,
                "drafting:lift": lift,
                "drafting:cf": cf,
                "drafting:subConfidenceRatio": subconfidenceratio,
                "drafting:supportX": support_x,
                "drafting:supportY": support_y,
            }
        )
        self._node_reference_vars(
            **{
                "drafting:machineLearningJob": ml_job,
            }
        )


directory = {
    "drafting:PassiveDnsFacet": FacetPassiveDNS,
    "drafting:TornodeInfoFacet": FacetTornodeInfo,
    "drafting:LocalInternetRegistryFacet": FacetLocalInternetRegistry,
    "drafting:ObservablePort": ObservablePort,
    "drafting:BlockHasherScanFacet": FacetBlockHasherScan,
    "drafting:BlockHasherUploadFacet": FacetBlockHasherUpload,
    "drafting:SocialMediaActivityFacet": FacetSocialMediaActivity,
    "drafting:dump": FacetNIO,
    "drafting:machineLearningResultFacet": FacetMachineLearningResults,
    "drafting:anprLog": FacetAnpr,
    "drafting:BlockHasherScanFacet": FacetBlockHasherScan,
    "drafting:BlockHasherUploadFacet": FacetBlockHasherUpload,
    "drafting:MachineLearningJobFacet": FacetMachineLearningJob,
    "drafting:NerEntityFacet": FacetNerEntity,
    "drafting:ExtractedUrlFacet": FacetExtractedUrl,
    "drafting:TranslationResultFacet": FacetTranslationResult,
    "drafting:LanguageDetectionResultFacet": FacetLanguageDetectionResult,
    "drafting:ExtractedTopicFacet": FacetExtractedTopic,
    "drafting:SentimentAnalysisResultFacet": FacetSentimentAnalysisResult,
    "drafting:TextSummarizationResultFacet": FacetTextSummarizationResult,
    "drafting:TextAnnotationResultFacet": FacetTextAnnotationResult,
    "drafting:TextIntervalFacet": FacetTextInterval,
    "drafting:TextIntervals": TextIntervals,
    "drafting:StylometryResultsFacet": FacetStylometryResults,
    "drafting:StylometrySimilarityFacet": FacetStylometrySimilarity,
    "drafting:DocumentCollectionFacet": FacetDocumentCollection,
    "drafting:KddKeyInfoFacet": FacetKddKeyInfo,
    "drafting:KddValueInfoFacet": FacetKddValueInfo,
    "drafting:KddKeyCombinationFacet": FacetKddKeyCombination,
    "drafting:KddKeyRuleFacet": FacetKddKeyRule,
}
