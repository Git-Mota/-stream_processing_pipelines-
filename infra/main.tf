resource "aws_s3_bucket" "events_bucket" {
  bucket = "shoptrend-events-stream-firehose"
}

resource "aws_kinesis_stream" "events_stream" {
  name             = "shoptrend-events-stream"
  shard_count      = 1
  retention_period = 24
}

resource "aws_kinesis_firehose_delivery_stream" "events_firehose" {
  name        = "shoptrend-events-stream-firehose"
  destination = "extended_s3"

  kinesis_source_configuration {
    kinesis_stream_arn = aws_kinesis_stream.events_stream.arn
    role_arn           = "arn:aws:iam::${var.aws_account_id}:role/LabRole"
  }

  extended_s3_configuration {
    bucket_arn = aws_s3_bucket.events_bucket.arn
    role_arn   = "arn:aws:iam::${var.aws_account_id}:role/LabRole"

    prefix              = "raw/events/!{timestamp:yyyy}/!{timestamp:MM}/!{timestamp:dd}/"
    error_output_prefix = "raw/errors/!{firehose:error-output-type}/"

    buffering_size     = 1
    buffering_interval = 60

    compression_format = "GZIP"
  }
}

