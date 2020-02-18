// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: entities.proto

package com.ververica.statefun.workshop.generated;

/**
 * <pre>
 * This message is sent from a MerchantFunction
 * instance when reporting the trustworthiness
 * of a merchant.
 * </pre>
 *
 * Protobuf type {@code MerchantScore}
 */
public  final class MerchantScore extends
    com.google.protobuf.GeneratedMessageV3 implements
    // @@protoc_insertion_point(message_implements:MerchantScore)
    MerchantScoreOrBuilder {
private static final long serialVersionUID = 0L;
  // Use MerchantScore.newBuilder() to construct.
  private MerchantScore(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
    super(builder);
  }
  private MerchantScore() {
  }

  @java.lang.Override
  public final com.google.protobuf.UnknownFieldSet
  getUnknownFields() {
    return this.unknownFields;
  }
  private MerchantScore(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    this();
    if (extensionRegistry == null) {
      throw new java.lang.NullPointerException();
    }
    int mutable_bitField0_ = 0;
    com.google.protobuf.UnknownFieldSet.Builder unknownFields =
        com.google.protobuf.UnknownFieldSet.newBuilder();
    try {
      boolean done = false;
      while (!done) {
        int tag = input.readTag();
        switch (tag) {
          case 0:
            done = true;
            break;
          case 8: {

            score_ = input.readInt32();
            break;
          }
          case 16: {

            error_ = input.readBool();
            break;
          }
          default: {
            if (!parseUnknownField(
                input, unknownFields, extensionRegistry, tag)) {
              done = true;
            }
            break;
          }
        }
      }
    } catch (com.google.protobuf.InvalidProtocolBufferException e) {
      throw e.setUnfinishedMessage(this);
    } catch (java.io.IOException e) {
      throw new com.google.protobuf.InvalidProtocolBufferException(
          e).setUnfinishedMessage(this);
    } finally {
      this.unknownFields = unknownFields.build();
      makeExtensionsImmutable();
    }
  }
  public static final com.google.protobuf.Descriptors.Descriptor
      getDescriptor() {
    return com.ververica.statefun.workshop.generated.Entities.internal_static_MerchantScore_descriptor;
  }

  @java.lang.Override
  protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internalGetFieldAccessorTable() {
    return com.ververica.statefun.workshop.generated.Entities.internal_static_MerchantScore_fieldAccessorTable
        .ensureFieldAccessorsInitialized(
            com.ververica.statefun.workshop.generated.MerchantScore.class, com.ververica.statefun.workshop.generated.MerchantScore.Builder.class);
  }

  public static final int SCORE_FIELD_NUMBER = 1;
  private int score_;
  /**
   * <code>int32 score = 1;</code>
   */
  public int getScore() {
    return score_;
  }

  public static final int ERROR_FIELD_NUMBER = 2;
  private boolean error_;
  /**
   * <code>bool error = 2;</code>
   */
  public boolean getError() {
    return error_;
  }

  private byte memoizedIsInitialized = -1;
  @java.lang.Override
  public final boolean isInitialized() {
    byte isInitialized = memoizedIsInitialized;
    if (isInitialized == 1) return true;
    if (isInitialized == 0) return false;

    memoizedIsInitialized = 1;
    return true;
  }

  @java.lang.Override
  public void writeTo(com.google.protobuf.CodedOutputStream output)
                      throws java.io.IOException {
    if (score_ != 0) {
      output.writeInt32(1, score_);
    }
    if (error_ != false) {
      output.writeBool(2, error_);
    }
    unknownFields.writeTo(output);
  }

  @java.lang.Override
  public int getSerializedSize() {
    int size = memoizedSize;
    if (size != -1) return size;

    size = 0;
    if (score_ != 0) {
      size += com.google.protobuf.CodedOutputStream
        .computeInt32Size(1, score_);
    }
    if (error_ != false) {
      size += com.google.protobuf.CodedOutputStream
        .computeBoolSize(2, error_);
    }
    size += unknownFields.getSerializedSize();
    memoizedSize = size;
    return size;
  }

  @java.lang.Override
  public boolean equals(final java.lang.Object obj) {
    if (obj == this) {
     return true;
    }
    if (!(obj instanceof com.ververica.statefun.workshop.generated.MerchantScore)) {
      return super.equals(obj);
    }
    com.ververica.statefun.workshop.generated.MerchantScore other = (com.ververica.statefun.workshop.generated.MerchantScore) obj;

    if (getScore()
        != other.getScore()) return false;
    if (getError()
        != other.getError()) return false;
    if (!unknownFields.equals(other.unknownFields)) return false;
    return true;
  }

  @java.lang.Override
  public int hashCode() {
    if (memoizedHashCode != 0) {
      return memoizedHashCode;
    }
    int hash = 41;
    hash = (19 * hash) + getDescriptor().hashCode();
    hash = (37 * hash) + SCORE_FIELD_NUMBER;
    hash = (53 * hash) + getScore();
    hash = (37 * hash) + ERROR_FIELD_NUMBER;
    hash = (53 * hash) + com.google.protobuf.Internal.hashBoolean(
        getError());
    hash = (29 * hash) + unknownFields.hashCode();
    memoizedHashCode = hash;
    return hash;
  }

  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      java.nio.ByteBuffer data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      java.nio.ByteBuffer data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      com.google.protobuf.ByteString data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      com.google.protobuf.ByteString data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(byte[] data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      byte[] data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseDelimitedFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseDelimitedFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      com.google.protobuf.CodedInputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static com.ververica.statefun.workshop.generated.MerchantScore parseFrom(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }

  @java.lang.Override
  public Builder newBuilderForType() { return newBuilder(); }
  public static Builder newBuilder() {
    return DEFAULT_INSTANCE.toBuilder();
  }
  public static Builder newBuilder(com.ververica.statefun.workshop.generated.MerchantScore prototype) {
    return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
  }
  @java.lang.Override
  public Builder toBuilder() {
    return this == DEFAULT_INSTANCE
        ? new Builder() : new Builder().mergeFrom(this);
  }

  @java.lang.Override
  protected Builder newBuilderForType(
      com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
    Builder builder = new Builder(parent);
    return builder;
  }
  /**
   * <pre>
   * This message is sent from a MerchantFunction
   * instance when reporting the trustworthiness
   * of a merchant.
   * </pre>
   *
   * Protobuf type {@code MerchantScore}
   */
  public static final class Builder extends
      com.google.protobuf.GeneratedMessageV3.Builder<Builder> implements
      // @@protoc_insertion_point(builder_implements:MerchantScore)
      com.ververica.statefun.workshop.generated.MerchantScoreOrBuilder {
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return com.ververica.statefun.workshop.generated.Entities.internal_static_MerchantScore_descriptor;
    }

    @java.lang.Override
    protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return com.ververica.statefun.workshop.generated.Entities.internal_static_MerchantScore_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              com.ververica.statefun.workshop.generated.MerchantScore.class, com.ververica.statefun.workshop.generated.MerchantScore.Builder.class);
    }

    // Construct using com.ververica.statefun.workshop.generated.MerchantScore.newBuilder()
    private Builder() {
      maybeForceBuilderInitialization();
    }

    private Builder(
        com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
      super(parent);
      maybeForceBuilderInitialization();
    }
    private void maybeForceBuilderInitialization() {
      if (com.google.protobuf.GeneratedMessageV3
              .alwaysUseFieldBuilders) {
      }
    }
    @java.lang.Override
    public Builder clear() {
      super.clear();
      score_ = 0;

      error_ = false;

      return this;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.Descriptor
        getDescriptorForType() {
      return com.ververica.statefun.workshop.generated.Entities.internal_static_MerchantScore_descriptor;
    }

    @java.lang.Override
    public com.ververica.statefun.workshop.generated.MerchantScore getDefaultInstanceForType() {
      return com.ververica.statefun.workshop.generated.MerchantScore.getDefaultInstance();
    }

    @java.lang.Override
    public com.ververica.statefun.workshop.generated.MerchantScore build() {
      com.ververica.statefun.workshop.generated.MerchantScore result = buildPartial();
      if (!result.isInitialized()) {
        throw newUninitializedMessageException(result);
      }
      return result;
    }

    @java.lang.Override
    public com.ververica.statefun.workshop.generated.MerchantScore buildPartial() {
      com.ververica.statefun.workshop.generated.MerchantScore result = new com.ververica.statefun.workshop.generated.MerchantScore(this);
      result.score_ = score_;
      result.error_ = error_;
      onBuilt();
      return result;
    }

    @java.lang.Override
    public Builder clone() {
      return super.clone();
    }
    @java.lang.Override
    public Builder setField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        java.lang.Object value) {
      return super.setField(field, value);
    }
    @java.lang.Override
    public Builder clearField(
        com.google.protobuf.Descriptors.FieldDescriptor field) {
      return super.clearField(field);
    }
    @java.lang.Override
    public Builder clearOneof(
        com.google.protobuf.Descriptors.OneofDescriptor oneof) {
      return super.clearOneof(oneof);
    }
    @java.lang.Override
    public Builder setRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        int index, java.lang.Object value) {
      return super.setRepeatedField(field, index, value);
    }
    @java.lang.Override
    public Builder addRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        java.lang.Object value) {
      return super.addRepeatedField(field, value);
    }
    @java.lang.Override
    public Builder mergeFrom(com.google.protobuf.Message other) {
      if (other instanceof com.ververica.statefun.workshop.generated.MerchantScore) {
        return mergeFrom((com.ververica.statefun.workshop.generated.MerchantScore)other);
      } else {
        super.mergeFrom(other);
        return this;
      }
    }

    public Builder mergeFrom(com.ververica.statefun.workshop.generated.MerchantScore other) {
      if (other == com.ververica.statefun.workshop.generated.MerchantScore.getDefaultInstance()) return this;
      if (other.getScore() != 0) {
        setScore(other.getScore());
      }
      if (other.getError() != false) {
        setError(other.getError());
      }
      this.mergeUnknownFields(other.unknownFields);
      onChanged();
      return this;
    }

    @java.lang.Override
    public final boolean isInitialized() {
      return true;
    }

    @java.lang.Override
    public Builder mergeFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      com.ververica.statefun.workshop.generated.MerchantScore parsedMessage = null;
      try {
        parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        parsedMessage = (com.ververica.statefun.workshop.generated.MerchantScore) e.getUnfinishedMessage();
        throw e.unwrapIOException();
      } finally {
        if (parsedMessage != null) {
          mergeFrom(parsedMessage);
        }
      }
      return this;
    }

    private int score_ ;
    /**
     * <code>int32 score = 1;</code>
     */
    public int getScore() {
      return score_;
    }
    /**
     * <code>int32 score = 1;</code>
     */
    public Builder setScore(int value) {
      
      score_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>int32 score = 1;</code>
     */
    public Builder clearScore() {
      
      score_ = 0;
      onChanged();
      return this;
    }

    private boolean error_ ;
    /**
     * <code>bool error = 2;</code>
     */
    public boolean getError() {
      return error_;
    }
    /**
     * <code>bool error = 2;</code>
     */
    public Builder setError(boolean value) {
      
      error_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>bool error = 2;</code>
     */
    public Builder clearError() {
      
      error_ = false;
      onChanged();
      return this;
    }
    @java.lang.Override
    public final Builder setUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return super.setUnknownFields(unknownFields);
    }

    @java.lang.Override
    public final Builder mergeUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return super.mergeUnknownFields(unknownFields);
    }


    // @@protoc_insertion_point(builder_scope:MerchantScore)
  }

  // @@protoc_insertion_point(class_scope:MerchantScore)
  private static final com.ververica.statefun.workshop.generated.MerchantScore DEFAULT_INSTANCE;
  static {
    DEFAULT_INSTANCE = new com.ververica.statefun.workshop.generated.MerchantScore();
  }

  public static com.ververica.statefun.workshop.generated.MerchantScore getDefaultInstance() {
    return DEFAULT_INSTANCE;
  }

  private static final com.google.protobuf.Parser<MerchantScore>
      PARSER = new com.google.protobuf.AbstractParser<MerchantScore>() {
    @java.lang.Override
    public MerchantScore parsePartialFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return new MerchantScore(input, extensionRegistry);
    }
  };

  public static com.google.protobuf.Parser<MerchantScore> parser() {
    return PARSER;
  }

  @java.lang.Override
  public com.google.protobuf.Parser<MerchantScore> getParserForType() {
    return PARSER;
  }

  @java.lang.Override
  public com.ververica.statefun.workshop.generated.MerchantScore getDefaultInstanceForType() {
    return DEFAULT_INSTANCE;
  }

}

