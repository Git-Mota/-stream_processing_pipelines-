output "kinesis_stream_name" {
  value = aws_kinesis_stream.events_stream.name
}

output "firehose_name" {
  value = aws_kinesis_firehose_delivery_stream.events_firehose.name
}

output "s3_bucket" {
  value = aws_s3_bucket.events_bucket.bucket
}