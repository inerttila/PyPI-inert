import fire

from inert.benchmarks import run_cli as benchmarks
from inert.classify.predict import run as classify_predict
from inert.classify.train import run_cli as classify_train
from inert.classify.val import run as classify_val
from inert.detect import run as detect
from inert.export import run as export
from inert.segment.predict import run as segment_predict
from inert.segment.train import run_cli as segment_train
from inert.segment.val import run as segment_val
from inert.train import run_cli as train
from inert.val import run as val


def app() -> None:
    """Cli app."""
    fire.Fire(
        {
            "train": train,
            "val": val,
            "detect": detect,
            "export": export,
            "benchmarks": benchmarks,
            'classify': {'train': classify_train, 'val': classify_val, 'predict': classify_predict},
            'segment': {'train': segment_train, 'val': segment_val, 'predict': segment_predict},
        }
    )

if __name__ == "__main__":
    app()
