from dataclass import dataclass
from torch.utils.data.dataloader import dataLoader

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str
