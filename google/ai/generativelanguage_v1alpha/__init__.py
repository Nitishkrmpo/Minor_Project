# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.ai.generativelanguage_v1alpha import gapic_version as package_version

__version__ = package_version.__version__


from .services.cache_service import CacheServiceAsyncClient, CacheServiceClient
from .services.discuss_service import DiscussServiceAsyncClient, DiscussServiceClient
from .services.file_service import FileServiceAsyncClient, FileServiceClient
from .services.generative_service import (
    GenerativeServiceAsyncClient,
    GenerativeServiceClient,
)
from .services.model_service import ModelServiceAsyncClient, ModelServiceClient
from .services.permission_service import (
    PermissionServiceAsyncClient,
    PermissionServiceClient,
)
from .services.prediction_service import (
    PredictionServiceAsyncClient,
    PredictionServiceClient,
)
from .services.retriever_service import (
    RetrieverServiceAsyncClient,
    RetrieverServiceClient,
)
from .services.text_service import TextServiceAsyncClient, TextServiceClient
from .types.cache_service import (
    CreateCachedContentRequest,
    DeleteCachedContentRequest,
    GetCachedContentRequest,
    ListCachedContentsRequest,
    ListCachedContentsResponse,
    UpdateCachedContentRequest,
)
from .types.cached_content import CachedContent
from .types.citation import CitationMetadata, CitationSource
from .types.content import (
    Blob,
    CodeExecution,
    CodeExecutionResult,
    Content,
    DynamicRetrievalConfig,
    ExecutableCode,
    FileData,
    FunctionCall,
    FunctionCallingConfig,
    FunctionDeclaration,
    FunctionResponse,
    GoogleSearchRetrieval,
    GroundingPassage,
    GroundingPassages,
    Part,
    Schema,
    Tool,
    ToolConfig,
    Type,
)
from .types.discuss_service import (
    CountMessageTokensRequest,
    CountMessageTokensResponse,
    Example,
    GenerateMessageRequest,
    GenerateMessageResponse,
    Message,
    MessagePrompt,
)
from .types.file import File, VideoMetadata
from .types.file_service import (
    CreateFileRequest,
    CreateFileResponse,
    DeleteFileRequest,
    GetFileRequest,
    ListFilesRequest,
    ListFilesResponse,
)
from .types.generative_service import (
    AttributionSourceId,
    BatchEmbedContentsRequest,
    BatchEmbedContentsResponse,
    BidiGenerateContentClientContent,
    BidiGenerateContentClientMessage,
    BidiGenerateContentRealtimeInput,
    BidiGenerateContentServerContent,
    BidiGenerateContentServerMessage,
    BidiGenerateContentSetup,
    BidiGenerateContentSetupComplete,
    BidiGenerateContentToolCall,
    BidiGenerateContentToolCallCancellation,
    BidiGenerateContentToolResponse,
    Candidate,
    ContentEmbedding,
    CountTokensRequest,
    CountTokensResponse,
    EmbedContentRequest,
    EmbedContentResponse,
    GenerateAnswerRequest,
    GenerateAnswerResponse,
    GenerateContentRequest,
    GenerateContentResponse,
    GenerationConfig,
    GroundingAttribution,
    GroundingChunk,
    GroundingMetadata,
    GroundingSupport,
    LogprobsResult,
    PrebuiltVoiceConfig,
    RetrievalMetadata,
    SearchEntryPoint,
    Segment,
    SemanticRetrieverConfig,
    SpeechConfig,
    TaskType,
    VoiceConfig,
)
from .types.model import Model
from .types.model_service import (
    CreateTunedModelMetadata,
    CreateTunedModelRequest,
    DeleteTunedModelRequest,
    GetModelRequest,
    GetTunedModelRequest,
    ListModelsRequest,
    ListModelsResponse,
    ListTunedModelsRequest,
    ListTunedModelsResponse,
    UpdateTunedModelRequest,
)
from .types.permission import Permission
from .types.permission_service import (
    CreatePermissionRequest,
    DeletePermissionRequest,
    GetPermissionRequest,
    ListPermissionsRequest,
    ListPermissionsResponse,
    TransferOwnershipRequest,
    TransferOwnershipResponse,
    UpdatePermissionRequest,
)
from .types.prediction_service import PredictRequest, PredictResponse
from .types.retriever import (
    Chunk,
    ChunkData,
    Condition,
    Corpus,
    CustomMetadata,
    Document,
    MetadataFilter,
    StringList,
)
from .types.retriever_service import (
    BatchCreateChunksRequest,
    BatchCreateChunksResponse,
    BatchDeleteChunksRequest,
    BatchUpdateChunksRequest,
    BatchUpdateChunksResponse,
    CreateChunkRequest,
    CreateCorpusRequest,
    CreateDocumentRequest,
    DeleteChunkRequest,
    DeleteCorpusRequest,
    DeleteDocumentRequest,
    GetChunkRequest,
    GetCorpusRequest,
    GetDocumentRequest,
    ListChunksRequest,
    ListChunksResponse,
    ListCorporaRequest,
    ListCorporaResponse,
    ListDocumentsRequest,
    ListDocumentsResponse,
    QueryCorpusRequest,
    QueryCorpusResponse,
    QueryDocumentRequest,
    QueryDocumentResponse,
    RelevantChunk,
    UpdateChunkRequest,
    UpdateCorpusRequest,
    UpdateDocumentRequest,
)
from .types.safety import (
    ContentFilter,
    HarmCategory,
    SafetyFeedback,
    SafetyRating,
    SafetySetting,
)
from .types.text_service import (
    BatchEmbedTextRequest,
    BatchEmbedTextResponse,
    CountTextTokensRequest,
    CountTextTokensResponse,
    Embedding,
    EmbedTextRequest,
    EmbedTextResponse,
    GenerateTextRequest,
    GenerateTextResponse,
    TextCompletion,
    TextPrompt,
)
from .types.tuned_model import (
    Dataset,
    Hyperparameters,
    TunedModel,
    TunedModelSource,
    TuningContent,
    TuningExample,
    TuningExamples,
    TuningMultiturnExample,
    TuningPart,
    TuningSnapshot,
    TuningTask,
)

__all__ = (
    "CacheServiceAsyncClient",
    "DiscussServiceAsyncClient",
    "FileServiceAsyncClient",
    "GenerativeServiceAsyncClient",
    "ModelServiceAsyncClient",
    "PermissionServiceAsyncClient",
    "PredictionServiceAsyncClient",
    "RetrieverServiceAsyncClient",
    "TextServiceAsyncClient",
    "AttributionSourceId",
    "BatchCreateChunksRequest",
    "BatchCreateChunksResponse",
    "BatchDeleteChunksRequest",
    "BatchEmbedContentsRequest",
    "BatchEmbedContentsResponse",
    "BatchEmbedTextRequest",
    "BatchEmbedTextResponse",
    "BatchUpdateChunksRequest",
    "BatchUpdateChunksResponse",
    "BidiGenerateContentClientContent",
    "BidiGenerateContentClientMessage",
    "BidiGenerateContentRealtimeInput",
    "BidiGenerateContentServerContent",
    "BidiGenerateContentServerMessage",
    "BidiGenerateContentSetup",
    "BidiGenerateContentSetupComplete",
    "BidiGenerateContentToolCall",
    "BidiGenerateContentToolCallCancellation",
    "BidiGenerateContentToolResponse",
    "Blob",
    "CacheServiceClient",
    "CachedContent",
    "Candidate",
    "Chunk",
    "ChunkData",
    "CitationMetadata",
    "CitationSource",
    "CodeExecution",
    "CodeExecutionResult",
    "Condition",
    "Content",
    "ContentEmbedding",
    "ContentFilter",
    "Corpus",
    "CountMessageTokensRequest",
    "CountMessageTokensResponse",
    "CountTextTokensRequest",
    "CountTextTokensResponse",
    "CountTokensRequest",
    "CountTokensResponse",
    "CreateCachedContentRequest",
    "CreateChunkRequest",
    "CreateCorpusRequest",
    "CreateDocumentRequest",
    "CreateFileRequest",
    "CreateFileResponse",
    "CreatePermissionRequest",
    "CreateTunedModelMetadata",
    "CreateTunedModelRequest",
    "CustomMetadata",
    "Dataset",
    "DeleteCachedContentRequest",
    "DeleteChunkRequest",
    "DeleteCorpusRequest",
    "DeleteDocumentRequest",
    "DeleteFileRequest",
    "DeletePermissionRequest",
    "DeleteTunedModelRequest",
    "DiscussServiceClient",
    "Document",
    "DynamicRetrievalConfig",
    "EmbedContentRequest",
    "EmbedContentResponse",
    "EmbedTextRequest",
    "EmbedTextResponse",
    "Embedding",
    "Example",
    "ExecutableCode",
    "File",
    "FileData",
    "FileServiceClient",
    "FunctionCall",
    "FunctionCallingConfig",
    "FunctionDeclaration",
    "FunctionResponse",
    "GenerateAnswerRequest",
    "GenerateAnswerResponse",
    "GenerateContentRequest",
    "GenerateContentResponse",
    "GenerateMessageRequest",
    "GenerateMessageResponse",
    "GenerateTextRequest",
    "GenerateTextResponse",
    "GenerationConfig",
    "GenerativeServiceClient",
    "GetCachedContentRequest",
    "GetChunkRequest",
    "GetCorpusRequest",
    "GetDocumentRequest",
    "GetFileRequest",
    "GetModelRequest",
    "GetPermissionRequest",
    "GetTunedModelRequest",
    "GoogleSearchRetrieval",
    "GroundingAttribution",
    "GroundingChunk",
    "GroundingMetadata",
    "GroundingPassage",
    "GroundingPassages",
    "GroundingSupport",
    "HarmCategory",
    "Hyperparameters",
    "ListCachedContentsRequest",
    "ListCachedContentsResponse",
    "ListChunksRequest",
    "ListChunksResponse",
    "ListCorporaRequest",
    "ListCorporaResponse",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ListFilesRequest",
    "ListFilesResponse",
    "ListModelsRequest",
    "ListModelsResponse",
    "ListPermissionsRequest",
    "ListPermissionsResponse",
    "ListTunedModelsRequest",
    "ListTunedModelsResponse",
    "LogprobsResult",
    "Message",
    "MessagePrompt",
    "MetadataFilter",
    "Model",
    "ModelServiceClient",
    "Part",
    "Permission",
    "PermissionServiceClient",
    "PrebuiltVoiceConfig",
    "PredictRequest",
    "PredictResponse",
    "PredictionServiceClient",
    "QueryCorpusRequest",
    "QueryCorpusResponse",
    "QueryDocumentRequest",
    "QueryDocumentResponse",
    "RelevantChunk",
    "RetrievalMetadata",
    "RetrieverServiceClient",
    "SafetyFeedback",
    "SafetyRating",
    "SafetySetting",
    "Schema",
    "SearchEntryPoint",
    "Segment",
    "SemanticRetrieverConfig",
    "SpeechConfig",
    "StringList",
    "TaskType",
    "TextCompletion",
    "TextPrompt",
    "TextServiceClient",
    "Tool",
    "ToolConfig",
    "TransferOwnershipRequest",
    "TransferOwnershipResponse",
    "TunedModel",
    "TunedModelSource",
    "TuningContent",
    "TuningExample",
    "TuningExamples",
    "TuningMultiturnExample",
    "TuningPart",
    "TuningSnapshot",
    "TuningTask",
    "Type",
    "UpdateCachedContentRequest",
    "UpdateChunkRequest",
    "UpdateCorpusRequest",
    "UpdateDocumentRequest",
    "UpdatePermissionRequest",
    "UpdateTunedModelRequest",
    "VideoMetadata",
    "VoiceConfig",
)
