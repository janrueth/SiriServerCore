from siriObjects.baseObjects import ServerBoundCommand, ClientBoundCommand, AceObject

import uuid

class StartSpeech(ServerBoundCommand):
    classIdentifier = "StartSpeech"
    groupIdentifier = "com.apple.ace.speech"
    
    CodecPCM_Mono_16Bit_8000HzValue = "PCM_Mono_16Bit_8000Hz"
    CodecPCM_Mono_16Bit_11025HzValue = "PCM_Mono_16Bit_11025Hz"
    CodecPCM_Mono_16Bit_16000HzValue = "PCM_Mono_16Bit_16000Hz"
    CodecPCM_Mono_16Bit_22050HzValue = "PCM_Mono_16Bit_22050Hz"
    CodecPCM_Mono_16Bit_32000HzValue = "PCM_Mono_16Bit_32000Hz"
    CodecSpeex_NB_Quality7Value = "Speex_NB_Quality7"
    CodecSpeex_WB_Quality8Value =  "Speex_WB_Quality8"
    
    AudioSourceLineInValue = "LineIn"
    AudioSourceBuiltInMicValue = "BuiltInMic"
    AudioSourceWiredHeadsetMicValue = "WiredHeadsetMic"
    AudioSourceBluetoothHandsFreeDeviceValue = "BluetoothHandsFreeDevice"
    AudioSourceUsbAudioValue = "UsbAudio"

    MotionActivityUnknownValue = "Unknown"
    MotionActivityFrozenValue = "Frozen"
    MotionActivityStaticValue = "Static"
    MotionActivityMovingValue = "Moving"
    MotionActivityWalkingValue = "Walking"
    MotionActivityDrivingValue = "Driving"
    MotionActivityCyclingValue = "Cycling"
    MotionActivitySemiStationaryValue = "SemiStationary"
    MotionActivityRunningValue = "Running"
    MotionActivityMovingCoarseValue = "MovingCoarse"
    MotionActivityInVehicleFrozenValue =  "InVehicleFrozen"
    MotionActivityInVehicleStaticValue = "InVehicleStatic"
    MotionActivityWalkingSlowValue = "WalkingSlow"
    MotionActivityDrivingInHandValue = "DrivingInHand"
    MotionActivityDrivingOtherValue = "DrivingOther"

    DspTypeNoneValue = "None"
    DspTypeNoiseCancellationValue = "NoiseCancellation"
    def __init__(self, plist):
        self.origin = None # string
        self.noiseReductionLevel = None # number
        self.motionConfidence = None # number
        self.motionActivity = None # string
        self.headsetName = None # string
        self.headsetId = None # string
        self.headsetAddress = None # string
        self.dspStatus = None # string
        self.codec = None # int ?? -> string mapping
        self.audioSource = None # string
        super(StartSpeech, self).__init__(plist)

class StartSpeechRequest(StartSpeech):
    classIdentifier = "StartSpeechRequest"
    groupIdentifier = "com.apple.ace.speech"
    def __init__(self, plist):
        self.handsFree = None # bool
        super(StartSpeechRequest, self).__init__(plist)
    

class StartSpeechDictation(StartSpeech):
    classIdentifier = "StartSpeechDictation"
    groupIdentifier = "com.apple.ace.speech"
    
    FieldKeyboardReturnKeyDefaultValue =  "Default"
    FieldKeyboardReturnKeyGoValue = "Go"
    FieldKeyboardReturnKeyGoogleValue = "Google"
    FieldKeyboardReturnKeyJoinValue = "Join"
    FieldKeyboardReturnKeyNextValue = "Next"
    FieldKeyboardReturnKeyRouteValue = "Route"
    FieldKeyboardReturnKeySearchValue = "Search"
    FieldKeyboardReturnKeySendValue = "Send"
    FieldKeyboardReturnKeyYahooValue = "Yahoo"
    FieldKeyboardReturnKeyDoneValue = "Done"
    FieldKeyboardReturnKeyEmergencyCallValue = "EmergencyCall"

    FieldKeyboardTypeDefaultValue = "Default"
    FieldKeyboardTypeASCIICapableValue = "ASCIICapable"
    FieldKeyboardTypeAlphabetValue = "Alphabet"
    FieldKeyboardTypeNumbersAndPunctuationValue = "NumbersAndPunctuation"
    FieldKeyboardTypeNumberPadValue = "NumberPad"
    FieldKeyboardTypeDecimalPadValue = "DecimalPad"
    FieldKeyboardTypeURLValue = "URL"
    FieldKeyboardTypeEmailAddressValue = "EmailAddress"
    FieldKeyboardTypePhonePadValue = "PhonePad"
    FieldKeyboardTypeNamePhonePadValue = "NamePhonePad"
    FieldKeyboardTypeTwitterValue = "Twitter"

    def __init__(self, plist):
        self.selectedText = None # string
        self.region = None # string
        self.prefixText = None # string
        self.postfixText = None # string
        self.language = None # string
        self.keyboardType = None # string
        self.keyboardReturnKey = None # string
        self.interactionId = None # string
        self.fieldLabel = None # string
        self.fieldId = None # string
        self.censorSpeech = None # bool
        self.applicationVersion = None # string
        self.applicationName = None # string
        super(StartSpeechDictation, self).__init__(plist)

class SpeechPacket(ServerBoundCommand):
    classIdentifier = "SpeechPacket"
    groupIdentifier = "com.apple.ace.speech"
    
    def __init__(self, plist):
        self.packets = None # array
        self.packetNumber = None # int
        self.data = None # binary
        super(SpeechPacket, self).__init__(plist)

class FinishSpeech(ServerBoundCommand):
    classIdentifier = "FinishSpeech"
    groupIdentifier = "com.apple.ace.speech"

    def __init__(self, plist):
        self.packetCount = None # int
        self.orderedContext = None # array
        super(FinishSpeech, self).__init__(plist)

class SpeechFailure(ClientBoundCommand):
    FailureReasonTimeoutValue = "Timeout"
    FailureReasonCorruptValue = "Corrupt"
    FailureReasonInvalidValue = "Invalid"
    FailureReasonInaudibleValue = "Inaudible"
    FailureReasonErrorValue = "Error"
    FailureReasonRetryValue = "Retry"
    FailureReasonUnsupportedValue = "Unsupported"
    FailureReasonQuotaExceededValue = "QuotaExceeded"
    
    def __init__(self, refId, reasonDescription, reason=0):
        super(SpeechFailure, self).__init__("SpeechFailure", "com.apple.ace.speech", None, refId)
        self.reasonDescription = reasonDescription
        self.reason = reason
    
    def to_plist(self):
        self.add_property('reasonDescription')
        self.add_property('reason')
        return super(SpeechFailure, self).to_plist()


class SpeechRecognized(ClientBoundCommand):
    def __init__(self, refId, recognition, sessionId=str.upper(str(uuid.uuid4()))):
        super(SpeechRecognized, self).__init__("SpeechRecognized", "com.apple.ace.speech", None, refId)
        self.sessionId = sessionId
        self.recognition = recognition
        
    def to_plist(self):
        self.add_property('sessionId')
        self.add_property('recognition')
        return super(SpeechRecognized, self).to_plist()


class Recognition(AceObject):
    def __init__(self, phrases=None):
        super(Recognition, self).__init__("Recognition", "com.apple.ace.speech")
        self.phrases = phrases if phrases != None else []
    
    def to_plist(self):
        self.add_property('phrases')
        return super(Recognition, self).to_plist()

class Phrase(AceObject):
    def __init__(self, lowConfidence=False, interpretations=None):
        super(Phrase, self).__init__("Phrase", "com.apple.ace.speech")
        self.lowConfidence = lowConfidence
        self.interpretations = interpretations if interpretations != None else []
    
    def to_plist(self):
        self.add_property('lowConfidence')
        self.add_property('interpretations')
        return super(Phrase, self).to_plist()

class Interpretation(AceObject):
    def __init__(self, tokens=None):
        super(Interpretation, self).__init__("Interpretation", "com.apple.ace.speech")
        self.tokens = tokens if tokens != None else []
    
    def to_plist(self):
        self.add_property('tokens')
        return super(Interpretation, self).to_plist()

class Token(AceObject):    
    def __init__(self, text, startTime, endTime, confidenceScore, removeSpaceBefore, removeSpaceAfter):
        super(Token, self).__init__("Token", "com.apple.ace.speech")
        self.text = text
        self.startTime = startTime
        self.endTime = endTime
        self.confidenceScore = confidenceScore
        self.removeSpaceBefore = removeSpaceBefore
        self.removeSpaceAfter = removeSpaceAfter

    def to_plist(self):
        self.add_property('text')
        self.add_property('startTime')
        self.add_property('endTime')
        self.add_property('confidenceScore')
        self.add_property('removeSpaceBefore')
        self.add_property('removeSpaceAfter')
        return super(Token, self).to_plist()
